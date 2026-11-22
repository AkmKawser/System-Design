#!/usr/bin/env python3
"""
extract_highres_book_images.py

Extracts ultra-high-resolution (2000+ px) lossless raster images directly
from 'uml-diagramming.pdf', applies contrast and sharpness optimization,
and organizes them into chapter subdirectories under:
  Data_Ingestion/Books/umlBook/images/Chapter_XX_.../

Replaces low-clarity spline-traced vector blobs with crystal-clear,
original high-DPI diagram images.
"""

import os
import io
import re
import sys
import time
import warnings
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image, ImageOps, ImageEnhance
import pypdf

warnings.filterwarnings("ignore")

BASE_DIR = Path(__file__).resolve().parent.parent.parent
UML_DIR = BASE_DIR / "topics" / "0.FUNDAMENTALS" / "System Requirements" / "UML-DIAGRAMMING" / "Data_Ingestion" / "Books" / "umlBook"
PDF_PATH = UML_DIR / "uml-diagramming.pdf"
IMAGES_DIR = UML_DIR / "images"

# Import chapter metadata from generate_chapter_markdowns
sys.path.insert(0, str(Path(__file__).resolve().parent))
from generate_chapter_markdowns import CHAPTERS_METADATA, sanitize_filename

def clean_fig_name(caption: str) -> str:
    clean = re.sub(r"[^\w\s-]", "", caption)
    clean = re.sub(r"[\s-]+", "_", clean).strip("_")
    return clean[:50]

def collect_extraction_tasks():
    print(f"📖 Analyzing PDF images: {PDF_PATH.name}...")
    reader = pypdf.PdfReader(str(PDF_PATH))
    print(f"Total PDF pages: {len(reader.pages)}")

    tasks = []
    
    for ch_num, title, start_page, end_page in CHAPTERS_METADATA:
        ch_dir_name = f"Chapter_{ch_num:02d}_{sanitize_filename(title)[:40]}"
        ch_out_dir = IMAGES_DIR / ch_dir_name
        ch_out_dir.mkdir(parents=True, exist_ok=True)
        
        start_idx = start_page + 14
        end_idx = min(end_page + 14, len(reader.pages) - 1)
        
        for p_idx in range(start_idx, end_idx + 1):
            page = reader.pages[p_idx]
            imgs = page.images
            if not imgs:
                continue
                
            txt = page.extract_text() or ""
            figs = re.findall(r"(?:Figure|FIGURE)\s+(\d+\.\d+)\s+([A-Z0-9].*?)(?:\.|\n|$)", txt)
            unique_figs = []
            for f_num, f_title in figs:
                f_clean = f_title.strip()
                if not any(f[0] == f_num for f in unique_figs):
                    unique_figs.append((f_num, f_clean))
                    
            book_page = p_idx - 14
            for img_idx, img in enumerate(imgs):
                if img_idx < len(unique_figs):
                    f_num, f_title = unique_figs[img_idx]
                    f_num_clean = f_num.replace(".", "_")
                    fig_label = f"Figure_{f_num_clean}_{clean_fig_name(f_title)}"
                else:
                    fig_label = f"Ch{ch_num:02d}_p{book_page:03d}_img{img_idx+1:02d}"
                    
                png_filename = f"{fig_label}.png"
                png_path = ch_out_dir / png_filename
                
                # Deduplicate if name exists
                dup_idx = 1
                while png_path in [t["out_png"] for t in tasks]:
                    png_filename = f"{fig_label}_{dup_idx}.png"
                    png_path = ch_out_dir / png_filename
                    dup_idx += 1
                    
                tasks.append({
                    "ch_num": ch_num,
                    "ch_title": title,
                    "book_page": book_page,
                    "pdf_index": p_idx,
                    "img_idx": img_idx,
                    "img_data": img.data,
                    "out_png": png_path,
                    "fig_name": fig_label
                })
                
    print(f"Total image extraction tasks queued: {len(tasks)}")
    return tasks

def process_single_task(task_idx, task):
    out_png = task["out_png"]
    
    try:
        pil_img = Image.open(io.BytesIO(task["img_data"]))
        if pil_img.mode != "RGB":
            pil_img = pil_img.convert("RGB")
            
        # Optimize contrast: pure white background and deep crisp black ink
        sharp = ImageOps.autocontrast(pil_img, cutoff=1)
        enhancer = ImageEnhance.Sharpness(sharp)
        crisp = enhancer.enhance(1.4)
        
        # Save as optimized lossless PNG
        crisp.save(str(out_png), format="PNG", optimize=True)
        size_kb = out_png.stat().st_size // 1024
        return task_idx, True, size_kb, crisp.size
    except Exception as e:
        return task_idx, False, 0, str(e)

def main():
    start_total = time.time()
    tasks = collect_extraction_tasks()
    
    print(f"\n🚀 Starting parallel high-resolution extraction with 8 worker threads...")
    success_count = 0
    fail_count = 0
    
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(process_single_task, idx, t): idx for idx, t in enumerate(tasks)}
        
        for future in as_completed(futures):
            idx = futures[future]
            task = tasks[idx]
            try:
                _, success, size_kb, info = future.result()
                if success:
                    success_count += 1
                else:
                    fail_count += 1
                    print(f"❌ Failed: Ch {task['ch_num']:02d} {task['fig_name']} - {info}")
            except Exception as e:
                fail_count += 1
                print(f"❌ Exception: Ch {task['ch_num']:02d} {task['fig_name']} - {e}")
                
    elapsed = time.time() - start_total
    print(f"\n✨ Extraction Complete in {elapsed:.2f}s!")
    print(f"   Successfully extracted: {success_count} images")
    print(f"   Failed: {fail_count} images")

if __name__ == "__main__":
    main()
