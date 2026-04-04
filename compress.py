from PIL import Image
import os, glob

# Target: max dimension 1400px wide, quality 78 for photos
MAX_SIZE = (1400, 900)
QUALITY  = 78

images_dir = "images"
converted  = 0

for src in glob.glob(f"{images_dir}/*.jpg") + glob.glob(f"{images_dir}/*.jpeg") + glob.glob(f"{images_dir}/*.png"):
    # skip already-webp and logos
    base = os.path.splitext(src)[0]
    out  = base + ".webp"
    if os.path.exists(out):
        orig_kb = os.path.getsize(src) / 1024
        new_kb  = os.path.getsize(out) / 1024
        # only skip if webp is already smaller
        if new_kb < orig_kb:
            print(f"SKIP (webp exists): {os.path.basename(src)}")
            continue
    img = Image.open(src)
    img.thumbnail(MAX_SIZE, Image.LANCZOS)
    if img.mode in ("RGBA", "LA", "P"):
        img = img.convert("RGBA")
        img.save(out, "WEBP", quality=QUALITY, method=6)
    else:
        img = img.convert("RGB")
        img.save(out, "WEBP", quality=QUALITY, method=6)
    orig_kb = os.path.getsize(src) / 1024
    new_kb  = os.path.getsize(out) / 1024
    print(f"{os.path.basename(src)}: {orig_kb:.0f}KB → {new_kb:.0f}KB")
    converted += 1

print(f"\nDone. {converted} images converted.")
