import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_directory = sys.argv[2]

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

print(os.listdir(image_folder))

for filename in os.listdir(image_folder):
    img = Image.open(f"{image_folder}{filename}")
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_directory}{clean_name}.png', 'png')