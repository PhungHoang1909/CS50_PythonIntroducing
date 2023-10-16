import sys
from PIL import Image, ImageOps

# Check command-line arguments
if len(sys.argv) != 3:
    print("Usage: python shirt.py input.jpg output.jpg")
    sys.exit(1)

input_file = sys.argv[1]
output_file = sys.argv[2]

# Check file extensions
input_ext = input_file.split('.')[-1].lower()
output_ext = output_file.split('.')[-1].lower()

if input_ext not in ['jpg', 'jpeg', 'png'] or output_ext not in ['jpg', 'jpeg', 'png']:
    print("Input and output files must be .jpg, .jpeg, or .png")
    sys.exit(1)

if input_ext != output_ext:
    print("Input and output files must have the same extension")
    sys.exit(1)

# Open images
try:
    base_image = Image.open(input_file)
    overlay_image = Image.open('shirt.png')
except FileNotFoundError:
    print(f"File {input_file} or shirt.png not found.")
    sys.exit(1)

# Resize and crop base image to match overlay image
base_image = ImageOps.fit(base_image, overlay_image.size)

# Overlay images
base_image.paste(overlay_image, (0, 0), overlay_image)

# Save result
base_image.save(output_file)
