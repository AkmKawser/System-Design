"""
scripts/vectorize_book_images.py
Extracts and converts all images from '[BEST] UML Diagramming.pdf'
into Scalable Vector Graphics (.svg) files organized by chapter.
Uses visioncortex VTracer engine for high-fidelity vector path tracing.
"""

import os
import re
import sys
import time
import io
import warnings
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image
import pypdf
import vtracer

warnings.filterwarnings("ignore")

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT))
PDF_PATH = REPO_ROOT / "Skills_Input" / "books" / "Overall" / "[BEST] UML Diagramming.pdf"
VECTOR_DIR = REPO_ROOT / "Skills_Input" / "books" / "Overall" / "vector_images"
TEMP_DIR = REPO_ROOT / "Skills_Input" / "books" / "Overall" / "_temp_img"

VECTOR_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)

# Master list of all 40 chapters
from scripts.generate_chapter_markdowns import CHAPTERS_METADATA, sanitize_filename

def clean_fig_name(caption: str) -> str:
    clean = re.sub(r"[^\w\s-]", "", caption)
    clean = re.sub(r"[\s-]+", "_", clean).strip("_")
    return clean[:50]

def collect_image_tasks():
    print(f"📖 Analyzing PDF images: {PDF_PATH.name}...")
    reader = pypdf.PdfReader(str(PDF_PATH))
    print(f"Total pages: {len(reader.pages)}")

    tasks = []
    
    for ch_num, title, start_page, end_page in CHAPTERS_METADATA:
        ch_dir_name = f"Chapter_{ch_num:02d}_{sanitize_filename(title)[:40]}"
        ch_out_dir = VECTOR_DIR / ch_dir_name
        ch_out_dir.mkdir(parents=True, exist_ok=True)
        
        start_idx = start_page + 14
        end_idx = min(end_page + 14, len(reader.pages) - 1)
        
        fig_counter = 0
        for p_idx in range(start_idx, end_idx + 1):
            page = reader.pages[p_idx]
            imgs = page.images
            if not imgs:
                continue
                
            txt = page.extract_text() or ""
            # Extract figure captions on this page e.g. "Figure 2.4 UML usecase diagram"
            figs = re.findall(r"(?:Figure|FIGURE)\s+(\d+\.\d+)\s+([A-Z0-9].*?)(?:\.|\n|$)", txt)
            unique_figs = []
            for f_num, f_title in figs:
                f_clean = f_title.strip()
                if not any(f[0] == f_num for f in unique_figs):
                    unique_figs.append((f_num, f_clean))
                    
            book_page = p_idx - 14
            for img_idx, img in enumerate(imgs):
                # Determine meaningful filename
                if img_idx < len(unique_figs):
                    f_num, f_title = unique_figs[img_idx]
                    f_num_clean = f_num.replace(".", "_")
                    fig_label = f"Figure_{f_num_clean}_{clean_fig_name(f_title)}"
                else:
                    fig_label = f"Ch{ch_num:02d}_p{book_page:03d}_img{img_idx+1:02d}"
                    
                svg_filename = f"{fig_label}.svg"
                svg_path = ch_out_dir / svg_filename
                
                # Deduplicate if name exists
                dup_idx = 1
                while svg_path in [t["out_svg"] for t in tasks]:
                    svg_filename = f"{fig_label}_{dup_idx}.svg"
                    svg_path = ch_out_dir / svg_filename
                    dup_idx += 1
                    
                tasks.append({
                    "ch_num": ch_num,
                    "ch_title": title,
                    "book_page": book_page,
                    "pdf_index": p_idx,
                    "img_idx": img_idx,
                    "img_data": img.data,
                    "out_svg": svg_path,
                    "fig_name": fig_label
                })
                
    print(f"Total image conversion tasks queued: {len(tasks)}")
    return tasks

def process_single_task(task_idx, task):
    out_svg = task["out_svg"]
    # Skip if already generated
    if out_svg.exists() and out_svg.stat().st_size > 100:
        return task_idx, True, out_svg.stat().st_size, "Cached"
        
    tmp_png = TEMP_DIR / f"temp_{os.getpid()}_{task_idx}.png"
    try:
        pil_img = Image.open(io.BytesIO(task["img_data"]))
        if pil_img.mode not in ("RGB", "L"):
            pil_img = pil_img.convert("RGB")
            
        # Optional: downscale huge images > 2000px width to speed up vectorization
        max_dim = 1800
        if max(pil_img.size) > max_dim:
            scale = max_dim / max(pil_img.size)
            new_size = (int(pil_img.width * scale), int(pil_img.height * scale))
            pil_img = pil_img.resize(new_size, Image.Resampling.LANCZOS)
            
        pil_img.save(str(tmp_png), format="PNG")
        
        vtracer.convert_image_to_svg_py(str(tmp_png), str(out_svg))
        size = out_svg.stat().st_size
        return task_idx, True, size, "Converted"
    except Exception as e:
        return task_idx, False, 0, str(e)
    finally:
        if tmp_png.exists():
            try:
                tmp_png.unlink()
            except:
                pass

def main():
    start_total = time.time()
    tasks = collect_image_tasks()
    
    print(f"\n🚀 Starting parallel vectorization with 8 worker threads...")
    completed_count = 0
    success_count = 0
    fail_count = 0
    
    with ThreadPoolExecutor(max_workers=8) as executor:
        futures = {executor.submit(process_single_task, idx, t): idx for idx, t in enumerate(tasks)}
        
        for future in as_completed(futures):
            idx = futures[future]
            completed_count += 1
            task = tasks[idx]
            try:
                _, success, size, msg = future.result()
                if success:
                    success_count += 1
                else:
                    fail_count += 1
                    print(f"❌ Failed: Ch {task['ch_num']:02d} {task['fig_name']} - {msg}")
            except Exception as e:
                fail_count += 1
                print(f"❌ Exception in worker: {e}")
                
            if completed_count % 25 == 0 or completed_count == len(tasks):
                elapsed = time.time() - start_total
                rate = completed_count / elapsed if elapsed > 0 else 1
                remain = (len(tasks) - completed_count) / rate
                print(f"[{completed_count:03d}/{len(tasks):03d}] Vectorized ({success_count} ok, {fail_count} failed) - {rate:.1f} imgs/s - Est. {remain:.0f}s left")

    # Cleanup temp directory
    try:
        for f in TEMP_DIR.iterdir():
            f.unlink()
        TEMP_DIR.rmdir()
    except:
        pass
        
    total_time = time.time() - start_total
    print(f"\n✨ Vectorization Complete in {total_time:.1f}s!")
    print(f"   Successfully generated: {success_count} SVG vector images.")
    if fail_count > 0:
        print(f"   Failed conversions: {fail_count}")

    # Generate master README for vector images
    generate_vector_readme(tasks)

def generate_vector_readme(tasks):
    readme_path = VECTOR_DIR / "Vector_Images_Catalog.md"
    print(f"\n📑 Generating Vector Images Directory Hub: {readme_path.name}...")
    
    # Group tasks by chapter
    by_chapter = {}
    for t in tasks:
        ch = t["ch_num"]
        if ch not in by_chapter:
            by_chapter[ch] = []
        by_chapter[ch].append(t)
        
    lines = [
        "# UML Diagramming: Master Vector Images Archive",
        "",
        "This directory stores high-resolution **Scalable Vector Graphics (.svg)** converted from all diagrams and figures in *UML Diagramming: A Case Study Approach* by Dr. Suriya Sundaramoorthy.",
        "",
        f"- **Total Vector Images**: {len(tasks)} SVGs",
        "- **Format**: W3C Scalable Vector Graphics (SVG)",
        "- **Generator**: VisionCortex VTracer Engine",
        "- **Organization**: Partitioned by Chapter",
        "",
        "---",
        "",
        "## 📑 Vector Diagrams by Chapter",
        "",
        "| Chapter | Chapter Title | Total Vector Diagrams | Folder Reference |",
        "| :---: | :--- | :---: | :--- |"
    ]
    
    for ch_num, title, _, _ in CHAPTERS_METADATA:
        ch_tasks = by_chapter.get(ch_num, [])
        folder_name = f"Chapter_{ch_num:02d}_{sanitize_filename(title)[:40]}"
        lines.append(f"| `{ch_num:02d}` | **{title}** | {len(ch_tasks)} SVGs | [`{folder_name}/`]({folder_name}/) |")
        
    lines.extend([
        "",
        "---",
        "",
        "## 🖼️ Figure Highlights & Sample Previews",
        "",
        "| Chapter | Figure ID & Caption | Scalable Vector File |",
        "| :---: | :--- | :--- |"
    ])
    
    # Add notable samples
    sample_figs = [t for t in tasks if t["fig_name"].startswith("Figure_")][:50]
    for sf in sample_figs:
        rel_link = f"{sf['out_svg'].parent.name}/{sf['out_svg'].name}"
        lines.append(f"| Ch {sf['ch_num']:02d} | {sf['fig_name'].replace('_', ' ')} | [`{sf['out_svg'].name}`]({rel_link}) |")
        
    readme_path.write_text("\n".join(lines), encoding="utf-8")
    print(f"✓ Created {readme_path}")

if __name__ == "__main__":
    main()
