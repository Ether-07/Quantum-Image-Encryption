from PIL import Image
import numpy as np

from src.analysis.metrics import (
    analyze_image
)

from src.analysis.histogram import (
    calculate_histogram,
    histogram_uniformity_score
)

from src.analysis.differential import (
    calculate_npcr,
    calculate_uaci
)


original = np.asarray(
    Image.open(
        "images/test.png"
    ).convert("L"),
    dtype=np.uint8
)

encrypted = np.asarray(
    Image.open(
        "results/phase5_encrypted.png"
    ).convert("L"),
    dtype=np.uint8
)


print("=" * 60)
print("PHASE 6 SECURITY ANALYSIS")
print("=" * 60)


# ----------------------------------
# Original metrics
# ----------------------------------

original_metrics = analyze_image(
    original
)

print("\nORIGINAL IMAGE")
print("-" * 60)

for name, value in (
    original_metrics.items()
):

    print(
        f"{name:25}: "
        f"{value:.6f}"
    )


# ----------------------------------
# Encrypted metrics
# ----------------------------------

encrypted_metrics = analyze_image(
    encrypted
)

print("\nENCRYPTED IMAGE")
print("-" * 60)

for name, value in (
    encrypted_metrics.items()
):

    print(
        f"{name:25}: "
        f"{value:.6f}"
    )


# ----------------------------------
# Histogram
# ----------------------------------

histogram = calculate_histogram(
    encrypted
)

uniformity = (
    histogram_uniformity_score(
        histogram
    )
)

print("\nENCRYPTED HISTOGRAM")
print("-" * 60)

print(
    "Uniformity score:",
    f"{uniformity:.6f}"
)


# ----------------------------------
# Summary
# ----------------------------------

print("\nINTERPRETATION")
print("-" * 60)

print(
    "Ideal encrypted-image entropy "
    "is close to 8 bits."
)

print(
    "Ideal adjacent-pixel correlations "
    "are close to 0."
)

print(
    "Higher NPCR and appropriate UACI "
    "indicate stronger diffusion."
)   