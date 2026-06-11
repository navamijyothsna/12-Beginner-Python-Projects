# Photo Processor

A terminal-based image processing tool built with the Pillow library. Load any image, apply one or more operations — filters, adjustments, transforms — and save the result as a new file. The original is never overwritten; every output is saved with a descriptive suffix (e.g. `photo_grayscale.jpg`, `photo_blur.jpg`).

---

## Requirements

```
pip install Pillow
```

---

## How to Run

```
python photo_processor.py
```

---

## Supported Formats

JPEG, PNG, BMP, GIF, TIFF, WEBP

---

## How to Use

1. Enter the path to an image file
2. Pick an operation from the menu
3. Adjust parameters when prompted (blur radius, brightness level, etc.)
4. The processed image is saved automatically
5. Apply more operations or quit and process another image

---

## Operations

| # | Operation | Description |
|---|---|---|
| 1 | Grayscale | Removes all color |
| 2 | Sepia | Warm brownish vintage tone |
| 3 | Blur | Gaussian blur with adjustable radius |
| 4 | Sharpen | Enhances edge detail with adjustable factor |
| 5 | Brightness | Lighten or darken the image |
| 6 | Contrast | Increase or reduce tonal range |
| 7 | Saturation | Boost or reduce color intensity |
| 8 | Rotate | Rotate by any angle, with optional canvas expansion |
| 9 | Flip | Mirror horizontally or vertically |
| 10 | Resize | Set a new width and height in pixels |
| 11 | Crop | Trim to a specific region using pixel coordinates |
| 12 | Thumbnail | Resize proportionally to fit within a max dimension |
| 13 | Edge Detection | Highlights edges using FIND_EDGES filter |
| 14 | Emboss | Gives the image a raised, sculpted look |
| 15 | Invert Colors | Flips every pixel value to its opposite |
| 16 | Batch | Applies grayscale, sepia, blur, sharpen, brightness, and contrast all at once |

---

## Output Naming

Each operation saves a new file with a descriptive suffix so the original is preserved:

```
photo.jpg           ← original (untouched)
photo_grayscale.jpg
photo_sepia.jpg
photo_blur.jpg
photo_rotate90.jpg
photo_resize_800x600.jpg
photo_thumb_256.jpg
```

---

## Sample Session

```
Enter image path: /home/user/photos/portrait.jpg
  Loaded: portrait.jpg (1920x1080, RGB)

  --- Operations ---
   1. Grayscale
   2. Sepia
   3. Blur
   ...

  Choose an operation: 3

  Applying: Blur
  Blur radius [0.5–20.0, default 2.0]: 4
  Saved: /home/user/photos/portrait_blur.jpg
```

---

## Features

- 16 operations covering filters, color adjustments, and geometric transforms
- All outputs saved with descriptive suffixes — original never overwritten
- Adjustable parameters for blur, sharpen, brightness, contrast, saturation, rotate, resize, crop, and thumbnail
- Batch mode runs 6 common operations in one go
- Error handling for missing files, unsupported formats, and bad inputs
- Process multiple images in one session

---

## Concepts Practiced

| Concept | Where it appears |
|---|---|
| Pillow (`PIL`) | image loading, saving, filters, enhancements, transforms |
| `ImageFilter` | blur, sharpen, edge detection, emboss |
| `ImageEnhance` | brightness, contrast, saturation, sharpness |
| `ImageOps` | grayscale, sepia channel split, flip, mirror, invert |
| Functions | one function per operation, clean separation of concerns |
| Dictionaries | operation menu mapping keys to names and functions |
| `os` module | path handling, file existence check, output naming |
| Input validation | float/int range checks with defaults |
| Error handling | try/except around image loading and operations |
