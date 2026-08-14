from PIL import Image

from src.analysis.histogram import (
    calculate_histogram,
    histogram_uniformity_score
)


original = Image.open(
    "images/test.png"
).convert("L")

encrypted = Image.open(
    "results/phase5_encrypted.png"
).convert("L")


original_histogram = calculate_histogram(
    original
)

encrypted_histogram = calculate_histogram(
    encrypted
)


print("Original histogram:")

print(
    original_histogram
)


print("\nEncrypted histogram:")

print(
    encrypted_histogram
)


print("\nOriginal uniformity score:")

print(
    histogram_uniformity_score(
        original_histogram
    )
)


print("\nEncrypted uniformity score:")

print(
    histogram_uniformity_score(
        encrypted_histogram
    )
)