import os
import sys
from PIL import Image, ImageFilter, ImageEnhance, ImageOps


# --- Helpers ---

def load_image(path):
    if not os.path.exists(path):
        print(f"  Error: File not found — {path}")
        return None
    try:
        img = Image.open(path)
        print(f"  Loaded: {os.path.basename(path)} ({img.size[0]}x{img.size[1]}, {img.mode})")
        return img
    except Exception as e:
        print(f"  Error loading image: {e}")
        return None


def save_image(img, original_path, suffix):
    base, ext = os.path.splitext(original_path)
    out_path = f"{base}_{suffix}{ext}"
    img.save(out_path)
    print(f"  Saved: {out_path}")
    return out_path


def get_float(prompt, min_val, max_val, default):
    while True:
        raw = input(f"  {prompt} [{min_val}–{max_val}, default {default}]: ").strip()
        if raw == "":
            return default
        try:
            val = float(raw)
            if min_val <= val <= max_val:
                return val
            print(f"  Enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  Enter a valid number.")


def get_int(prompt, min_val, max_val, default):
    while True:
        raw = input(f"  {prompt} [{min_val}–{max_val}, default {default}]: ").strip()
        if raw == "":
            return default
        try:
            val = int(raw)
            if min_val <= val <= max_val:
                return val
            print(f"  Enter a value between {min_val} and {max_val}.")
        except ValueError:
            print("  Enter a valid integer.")


# --- Filters ---

def apply_grayscale(img, path):
    result = ImageOps.grayscale(img)
    save_image(result, path, "grayscale")


def apply_sepia(img, path):
    gray = ImageOps.grayscale(img).convert("RGB")
    r, g, b = gray.split()
    r = r.point(lambda i: min(255, int(i * 1.1)))
    g = g.point(lambda i: int(i * 0.9))
    b = b.point(lambda i: int(i * 0.7))
    result = Image.merge("RGB", (r, g, b))
    save_image(result, path, "sepia")


def apply_blur(img, path):
    radius = get_float("Blur radius", 0.5, 20.0, 2.0)
    result = img.filter(ImageFilter.GaussianBlur(radius=radius))
    save_image(result, path, "blur")


def apply_sharpen(img, path):
    factor = get_float("Sharpen factor", 1.0, 5.0, 2.0)
    result = ImageEnhance.Sharpness(img).enhance(factor)
    save_image(result, path, "sharpen")


def apply_brightness(img, path):
    factor = get_float("Brightness factor (1.0 = original)", 0.1, 5.0, 1.5)
    result = ImageEnhance.Brightness(img).enhance(factor)
    save_image(result, path, "brightness")


def apply_contrast(img, path):
    factor = get_float("Contrast factor (1.0 = original)", 0.1, 5.0, 1.5)
    result = ImageEnhance.Contrast(img).enhance(factor)
    save_image(result, path, "contrast")


def apply_saturation(img, path):
    factor = get_float("Saturation factor (1.0 = original, 0 = grayscale)", 0.0, 5.0, 1.5)
    result = ImageEnhance.Color(img).enhance(factor)
    save_image(result, path, "saturation")


def apply_rotate(img, path):
    angle = get_int("Rotation angle (degrees)", 1, 360, 90)
    expand = input("  Expand canvas to fit? (y/n, default y): ").strip().lower()
    expand = expand != "n"
    result = img.rotate(angle, expand=expand)
    save_image(result, path, f"rotate{angle}")


def apply_flip(img, path):
    print("  Flip direction: 1. Horizontal  2. Vertical")
    while True:
        choice = input("  Enter choice: ").strip()
        if choice == "1":
            result = ImageOps.mirror(img)
            save_image(result, path, "flip_h")
            break
        elif choice == "2":
            result = ImageOps.flip(img)
            save_image(result, path, "flip_v")
            break
        print("  Enter 1 or 2.")


def apply_resize(img, path):
    print(f"  Current size: {img.size[0]}x{img.size[1]}")
    w = get_int("New width (px)", 1, 10000, img.size[0] // 2)
    h = get_int("New height (px)", 1, 10000, img.size[1] // 2)
    result = img.resize((w, h), Image.LANCZOS)
    save_image(result, path, f"resize_{w}x{h}")


def apply_crop(img, path):
    W, H = img.size
    print(f"  Image size: {W}x{H}")
    left   = get_int("Left (px)", 0, W - 1, 0)
    top    = get_int("Top (px)", 0, H - 1, 0)
    right  = get_int("Right (px)", left + 1, W, W)
    bottom = get_int("Bottom (px)", top + 1, H, H)
    result = img.crop((left, top, right, bottom))
    save_image(result, path, "crop")


def apply_thumbnail(img, path):
    size = get_int("Max dimension (px)", 16, 2000, 256)
    result = img.copy()
    result.thumbnail((size, size), Image.LANCZOS)
    save_image(result, path, f"thumb_{size}")


def apply_edge_detect(img, path):
    gray   = ImageOps.grayscale(img)
    result = gray.filter(ImageFilter.FIND_EDGES)
    save_image(result, path, "edges")


def apply_emboss(img, path):
    result = img.filter(ImageFilter.EMBOSS)
    save_image(result, path, "emboss")


def apply_invert(img, path):
    rgb    = img.convert("RGB")
    result = ImageOps.invert(rgb)
    save_image(result, path, "invert")


def apply_batch(img, path):
    print("\n  Batch: applying grayscale, sepia, blur, sharpen, brightness, contrast.")
    apply_grayscale(img, path)
    apply_sepia(img, path)
    apply_blur(img, path)
    apply_sharpen(img, path)
    apply_brightness(img, path)
    apply_contrast(img, path)


# --- Menu ---

OPERATIONS = {
    "1":  ("Grayscale",       apply_grayscale),
    "2":  ("Sepia",           apply_sepia),
    "3":  ("Blur",            apply_blur),
    "4":  ("Sharpen",         apply_sharpen),
    "5":  ("Brightness",      apply_brightness),
    "6":  ("Contrast",        apply_contrast),
    "7":  ("Saturation",      apply_saturation),
    "8":  ("Rotate",          apply_rotate),
    "9":  ("Flip",            apply_flip),
    "10": ("Resize",          apply_resize),
    "11": ("Crop",            apply_crop),
    "12": ("Thumbnail",       apply_thumbnail),
    "13": ("Edge Detection",  apply_edge_detect),
    "14": ("Emboss",          apply_emboss),
    "15": ("Invert Colors",   apply_invert),
    "16": ("Batch (all)",     apply_batch),
}


def show_menu():
    print("\n  --- Operations ---")
    for key, (name, _) in OPERATIONS.items():
        print(f"  {key:>2}. {name}")
    print("   q. Quit")


def pick_image():
    while True:
        path = input("\nEnter image path: ").strip().strip('"')
        img = load_image(path)
        if img:
            return img, path
        retry = input("  Try another path? (y/n): ").strip().lower()
        if retry != "y":
            return None, None


def process_another():
    return input("\nProcess another image? (y/n): ").strip().lower() == "y"


def main():
    print("Welcome to Photo Processor!")
    print("Supported formats: JPEG, PNG, BMP, GIF, TIFF, WEBP\n")

    while True:
        img, path = pick_image()
        if img is None:
            break

        while True:
            show_menu()
            choice = input("\n  Choose an operation: ").strip().lower()

            if choice == "q":
                break
            elif choice in OPERATIONS:
                name, fn = OPERATIONS[choice]
                print(f"\n  Applying: {name}")
                try:
                    fn(img, path)
                except Exception as e:
                    print(f"  Error: {e}")
            else:
                print("  Invalid choice.")

        if not process_another():
            print("\nGoodbye!\n")
            break


if __name__ == "__main__":
    main()
