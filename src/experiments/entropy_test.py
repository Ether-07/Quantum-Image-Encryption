from PIL import Image

from src.analysis.entropy import (
    calculate_entropy
)


original = Image.open(
    "images/test.png"
).convert("L")

encrypted = Image.open(
    "results/phase5_encrypted.png"
).convert("L")


original_entropy = calculate_entropy(
    original
)

encrypted_entropy = calculate_entropy(
    encrypted
)


print(
    "Original entropy:"
)

print(
    f"{original_entropy:.6f}"
)


print(
    "\nEncrypted entropy:"
)

print(
    f"{encrypted_entropy:.6f}"
)


print(
    "\nMaximum possible entropy:"
)

print(
    "8.000000"
)