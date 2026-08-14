from PIL import Image
import numpy as np

input_path = "images/test.png"
output_path = "images/test_gray.png"

image = Image.open(input_path)

gray = image.convert("L")

gray.save(output_path)

pixels = np.array(gray)

print("Original mode:", image.mode)
print("Grayscale mode:", gray.mode)
print("Grayscale shape:", pixels.shape)
print("Minimum pixel:", pixels.min())
print("Maximum pixel:", pixels.max())