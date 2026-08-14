from PIL import Image
import numpy as np


original = np.asarray(
    Image.open(
        "images/test.png"
    ).convert("L"),
    dtype=np.uint8
)

encrypted = np.asarray(
    Image.open(
        "results/encrypted.png"
    ).convert("L"),
    dtype=np.uint8
)


difference = np.abs(
    original.astype(np.int16)
    -
    encrypted.astype(np.int16)
)


changed_pixels = np.count_nonzero(
    original != encrypted
)

total_pixels = original.size

change_percentage = (
    changed_pixels
    / total_pixels
) * 100


print("Total pixels:")
print(total_pixels)

print("\nChanged pixels:")
print(changed_pixels)

print("\nChanged pixel percentage:")
print(
    f"{change_percentage:.2f}%"
)

print("\nMaximum difference:")
print(difference.max())