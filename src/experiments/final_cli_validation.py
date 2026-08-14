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
        "results/final_decrypted.png"
    ).convert("L"),
    dtype=np.uint8
)


difference = np.abs(
    original.astype(np.int16)
    -
    decrypted.astype(np.int16)
)


print("=" * 60)
print("FINAL CLI VALIDATION")
print("=" * 60)

print(
    "\nImages identical:",
    np.array_equal(
        original,
        decrypted
    )
)

print(
    "\nMaximum pixel difference:",
    difference.max()
)

print(
    "\nTotal absolute difference:",
    difference.sum()
)