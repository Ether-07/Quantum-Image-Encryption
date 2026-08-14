from PIL import Image
import numpy as np

image = Image.open("test.png")

print("Image size:", image.size)
print("Image mode:", image.mode)

pixels = np.array(image)

print("Array shape:", pixels.shape)
print("First pixel:", pixels[0, 0])