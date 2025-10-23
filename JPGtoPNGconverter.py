import sys
import os
from PIL import Image

image_folder = sys.argv[1]
output_directory = sys.argv[2]

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for filename in os.