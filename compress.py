from PIL import Image
import os, glob

# Generate multiple sizes for srcset
SIZES = {
    "hero":    [(1400, 900, 75), (800, 520, 72), (480, 320, 68)],
    "large":   [(1200, 800, 75), (700, 480, 72), (400, 280, 68)],
    "medium":  [(900,  600, 78), (500, 340, 74)],
    "small":   [(600,  400, 80)],
}

# Map each image to a size category
IMAGE_MAP = {
    "olive tree granada":          "hero",
    "portugal square":             "hero",
    "rainbow umbrellas portugal":  "large",
    "portugal trams":              "large",
    "portugal trees":              "large",
    "Spain yellow alley":          "large",
    "spain dog walk":              "medium",
    "retired couple portugal":     "large",
    "couple spain":                "medium",
    "family at beach portugal":    "large",
    "young people cafe portugal":  "large",
    "student spain":               "medium",
    "young people portugal":       "large",
    "couple market portugal":      "large",
    "family portugal":             "large",
    "warm paperwork":              "medium",
    "young family portugal":       "medium",
    "retirement portugal":         "large",
    "pharmacy portugal":           "medium",
    "pharmacy sign":               "medium",
    "portugal sign":               "medium",
    "plaza de espana sign":        "medium",
    "spain cafe":                  "small",
    "couple portugal":             "small",
    "portugal family group":       "medium",
    "prescriptions":               "small",
    "clinic appointment":          "small",
    "portugal flag":               "small",
    "Spain flag":                  "small",
    "Spain sign":                  "small",
}

os.makedirs("images", exist_ok=True)

for base_name, size_key in IMAGE_MAP.items():
    # Find source file
    src = None
    for ext in [".jpg", ".jpeg", ".png"]:
        candidate = f"images/{base_name}{ext}"
        if os.path.exists(candidate):
            src = candidate
            break
    if not src:
        print(f"NOT FOUND: {base_name}")
        continue

    img_orig = Image.open(src)
    specs = SIZES[size_key]

    for i, (w, h, q) in enumerate(specs):
        img = img_orig.copy()
        img.thumbnail((w, h), Image.LANCZOS)

        if i == 0:
            out = f"images/{base_name}.webp"          # main (largest)
        else:
            out = f"images/{base_name}-{w}w.webp"     # responsive variant

        if img.mode in ("RGBA", "LA", "P"):
            img = img.convert("RGBA")
            img.save(out, "WEBP", quality=q, method=6)
        else:
            img = img.convert("RGB")
            img.save(out, "WEBP", quality=q, method=6)

        orig_kb = os.path.getsize(src) / 1024
        new_kb  = os.path.getsize(out) / 1024
        print(f"{os.path.basename(out)}: {new_kb:.0f}KB  (orig {orig_kb:.0f}KB)")

print("\nDone.")
