from PIL import Image
import numpy as np

from src.analysis.histogram import (
    calculate_histogram
)

from src.analysis.visualization import (
    plot_histograms
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


original_histogram = (
    calculate_histogram(
        original
    )
)

encrypted_histogram = (
    calculate_histogram(
        encrypted
    )
)


plot_histograms(
    original_histogram,
    encrypted_histogram,
    "docs/figures/histogram_comparison.png"
)


print(
    "Histogram figure generated:"
)

print(
    "docs/figures/histogram_comparison.png"
)