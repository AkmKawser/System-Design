from pathlib import Path
from playwright.sync_api import sync_playwright
from PIL import Image
import io

tasks = [
    {
        "svg": Path("animated_images/ui-api-backend-flow.svg"),
        "gif": Path("animated_images/ui-api-backend-flow.gif"),
        "duration_ms": 12000,
        "step_ms": 200, # 5 fps = 60 frames
        "viewport": {"width": 720, "height": 300},
        "colors": 128
    },
    {
        "svg": Path("animated_images/checkout-sequence-diagram.svg"),
        "gif": Path("animated_images/checkout-sequence-diagram.gif"),
        "duration_ms": 18000,
        "step_ms": 250, # 4 fps = 72 frames
        "viewport": {"width": 1020, "height": 820},
        "colors": 128
    }
]

with sync_playwright() as p:
    browser = p.chromium.launch()
    for task in tasks:
        svg_path = task["svg"].resolve()
        out_gif = task["gif"]
        print(f"\nProcessing {svg_path.name} -> {out_gif.name}...")
        
        page = browser.new_page(viewport=task["viewport"], device_scale_factor=1)
        page.goto(f"file:///{svg_path.as_posix()}")
        
        anims_count = page.evaluate("() => document.getAnimations().length")
        print(f"  Animations: {anims_count}")
        
        # Pause all animations
        page.evaluate("() => { document.getAnimations().forEach(a => a.pause()); }")
        
        frames = []
        svg_locator = page.locator("svg")
        
        dur = task["duration_ms"]
        step = task["step_ms"]
        
        for t in range(0, dur, step):
            page.evaluate(f"() => {{ document.getAnimations().forEach(a => a.currentTime = {t}); }}")
            png_bytes = svg_locator.screenshot()
            img = Image.open(io.BytesIO(png_bytes)).convert("RGB")
            frames.append(img)
            
        print(f"  Captured {len(frames)} frames. Quantizing to {task['colors']} colors...")
        p_frames = [f.quantize(colors=task["colors"], method=Image.Resampling.LANCZOS) for f in frames]
        
        p_frames[0].save(
            out_gif,
            save_all=True,
            append_images=p_frames[1:],
            duration=step,
            loop=0,
            optimize=True
        )
        print(f"  Saved {out_gif} ({out_gif.stat().st_size} bytes)")
        page.close()
        
    browser.close()
print("\nAll SVG to GIF conversions completed successfully!")
