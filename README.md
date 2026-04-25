# Random Wallpaper Selector

Small Windows script that picks a random image from the same folder as the script and sets it as the desktop wallpaper.

## What it does

- Scans the script directory for image files
- Supports `.jpg`, `.jpeg`, `.png`, `.bmp`, and `.webp`
- Chooses one image at random
- Updates the current user's Windows wallpaper using the system API

## Requirements

- Windows
- Python 3

No third-party packages are required.

## Usage

1. Put the images you want to use in the same folder as `set_random_wallpaper.py`.
2. Open a terminal in that folder.
3. Run:

```bash
python set_random_wallpaper.py
```

The script prints the image it selected and then waits for you to press Enter before closing.

## Example

If your folder looks like this:

```text
Random-Wallpaper-Selector/
  set_random_wallpaper.py
  beach.jpg
  mountain.png
  city.webp
```

Running the script will randomly choose one of those images and set it as your wallpaper.

## Notes

- The script only looks in the folder where it lives, not in subfolders.
- If no supported image files are found, it prints a message and exits.
- This changes the wallpaper for the current Windows user account only.

## Customization

If you want to use different image types, edit the `image_extensions` set in `set_random_wallpaper.py`.