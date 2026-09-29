import os
import shutil
from PIL import Image

src_path = r"C:\Users\Sachin\.gemini\antigravity\brain\c28d5128-dfa1-487c-8eca-e52f99ee40ad\.user_uploaded\media_1790665911472.jpg"
media_dir = r"C:\Users\Sachin\.gemini\antigravity\scratch\sachin_portfolio\media\profile"
static_dir = r"C:\Users\Sachin\.gemini\antigravity\scratch\sachin_portfolio\static\images"

os.makedirs(media_dir, exist_ok=True)
os.makedirs(static_dir, exist_ok=True)

# Copy original
target_media = os.path.join(media_dir, "sachin_profile.jpg")
target_static = os.path.join(static_dir, "sachin_profile.jpg")

shutil.copy2(src_path, target_media)
shutil.copy2(src_path, target_static)
print(f"Copied photo to {target_media} and {target_static}")

# Create an optimized circular portrait crop focusing on face/upper body
try:
    with Image.open(src_path) as img:
        width, height = img.size
        # Crop focusing on upper body (top ~60% of image with square aspect)
        crop_size = min(width, int(height * 0.75))
        left = (width - crop_size) // 2
        top = int(height * 0.08)
        right = left + crop_size
        bottom = top + crop_size
        
        cropped = img.crop((left, top, right, bottom))
        cropped.save(os.path.join(static_dir, "sachin_portrait.jpg"), quality=95)
        cropped.save(os.path.join(media_dir, "sachin_portrait.jpg"), quality=95)
        print("Created cropped portrait version successfully!")
except Exception as e:
    print("Crop error:", e)
