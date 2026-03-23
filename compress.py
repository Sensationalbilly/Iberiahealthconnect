from PIL import Image
import os

files = [
    ("Background.png",       (1920, 1080), 82),
    ("doctor.png",           (900,  1100), 88),
    ("Gemini_Generated_Image_xpxgpuxpxgpuxpxg copy (1).png", (900, 1100), 82),
    ("Gemini_Generated_Image_xpxgpuxpxgpuxpxg_copy-removebg-preview.png", (900, 1100), 82),
    ("IBERIA HEALTH.png",    (400,  200),  90),
    ("Logo PNG (1).png",     (400,  200),  90),
]

os.makedirs("images", exist_ok=True)

for filename, max_size, quality in files:
    if not os.path.exists(filename):
        print(f"SKIP (not found): {filename}")
        continue
    img = Image.open(filename)
    img.thumbnail(max_size, Image.LANCZOS)
    out_name = os.path.splitext(filename)[0] + ".webp"
    out_path = os.path.join("images", out_name)
    # preserve transparency if present
    if img.mode in ("RGBA", "LA"):
        img.save(out_path, "WEBP", quality=quality, method=6)
    else:
        img = img.convert("RGB")
        img.save(out_path, "WEBP", quality=quality, method=6)
    orig_kb  = os.path.getsize(filename) / 1024
    new_kb   = os.path.getsize(out_path) / 1024
    print(f"{filename}: {orig_kb:.0f}KB → {new_kb:.0f}KB  saved to images/{out_name}")

print("\nDone.")
