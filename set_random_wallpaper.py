import os
import random
import ctypes
import pathlib

def set_random_wallpaper():
    # Define common image extensions
    image_extensions = {'.jpg', '.jpeg', '.png', '.bmp', '.webp'}
    
    # Get the current directory path
    current_dir = pathlib.Path(__file__).parent.resolve()
    
    # List all files and filter for images
    images = [
        f for f in os.listdir(current_dir) 
        if pathlib.Path(f).suffix.lower() in image_extensions
    ]
    
    if not images:
        print("No image files found in the directory.")
        return

    # Select a random image
    random_image = random.choice(images)
    image_path = str(current_dir / random_image)
    
    print(f"Selecting random image: {random_image}")
    
    # Set the wallpaper using Windows SystemParametersInfoW
    # SPI_SETDESKWALLPAPER = 20
    # 3 = SPIF_UPDATEINIFILE | SPIF_SENDWININICHANGE
    result = ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)
    
    if result:
        print("Wallpaper successfully updated!")
    else:
        print("Failed to set wallpaper.")

if __name__ == "__main__":
    set_random_wallpaper()
    input("\nPress Enter to exit...")
