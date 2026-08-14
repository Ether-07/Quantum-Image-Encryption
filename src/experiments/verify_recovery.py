from PIL import Image
import numpy as np


original = np.asarray(
    Image.open(
        "images/test.png"
    ).convert("L"),
    dtype=np.uint8
)

decrypted = np.asarray(
    Image.open(
        "results/decrypted.png"
    ).convert("L"),
    dtype=np.uint8
)


print("Original shape:")
print(original.shape)

print("\nDecrypted shape:")
print(decrypted.shape)


same = np.array_equal(
    original,
    decrypted
)

print("\nImages identical:")
print(same)


difference = np.abs(
    original.astype(np.int16)
    -
    decrypted.astype(np.int16)
)


print("\nMaximum pixel difference:")
print(difference.max())


print("\nTotal absolute difference:")
print(difference.sum())