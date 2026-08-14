from PIL import Image
import numpy as np

image = Image.open("images/test.png")
pixels = np.array(image)

pixel = pixels[0, 0]

print("Pixel:", pixel)

for value in pixel:
    print(value, "=", format(value, "08b"))