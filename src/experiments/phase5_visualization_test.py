from pathlib import Path

import numpy as np
from PIL import Image

from src.analysis.histogram import (
    calculate_histogram
)

from src.analysis.correlation import (
    calculate_correlations
)

from src.analysis.metrics import (
    analyze_image
)

from src.analysis.visualization import (
    plot_histograms,
    plot_correlation_comparison,
    plot_security_metrics
)


# ============================================================
# PATHS
# ============================================================

ORIGINAL_PATH = (
    "images/test.png"
)

ENCRYPTED_PATH = (
    "results/phase5_encrypted.png"
)

OUTPUT_DIRECTORY = Path(
    "results/visualizations"
)

OUTPUT_DIRECTORY.mkdir(
    parents=True,
    exist_ok=True
)


# ============================================================
# LOAD IMAGES
# ============================================================

original = np.asarray(
    Image.open(
        ORIGINAL_PATH
    ).convert("L"),
    dtype=np.uint8
)

encrypted = np.asarray(
    Image.open(
        ENCRYPTED_PATH
    ).convert("L"),
    dtype=np.uint8
)


# ============================================================
# HISTOGRAMS
# ============================================================

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
    OUTPUT_DIRECTORY
    /
    "histogram_comparison.png"
)


# ============================================================
# CORRELATION
# ============================================================

original_correlations = (
    calculate_correlations(
        original
    )
)

encrypted_correlations = (
    calculate_correlations(
        encrypted
    )
)

plot_correlation_comparison(
    original_correlations,
    encrypted_correlations,
    OUTPUT_DIRECTORY
    /
    "correlation_comparison.png"
)


# ============================================================
# SECURITY METRICS
# ============================================================

original_metrics = (
    analyze_image(
        original
    )
)

encrypted_metrics = (
    analyze_image(
        encrypted
    )
)


# NOTE:
# NPCR and UACI are not calculated here because they
# require two ciphertexts. The Phase 4 GUI already
# calculates them using a one-pixel modified image.
#
# These values are based on the previous Phase 6
# experiment result for the current test image.

npcr = 99.707031
uaci = 33.590519

plot_security_metrics(
    encrypted_metrics["entropy"],
    npcr,
    uaci,
    OUTPUT_DIRECTORY
    /
    "security_metrics.png"
)


# ============================================================
# OUTPUT
# ============================================================

print("=" * 70)

print(
    "PHASE 5 - VISUALIZATION TEST"
)

print("=" * 70)

print()

print(
    "Generated:"
)

print(
    OUTPUT_DIRECTORY
    /
    "histogram_comparison.png"
)

print(
    OUTPUT_DIRECTORY
    /
    "correlation_comparison.png"
)

print(
    OUTPUT_DIRECTORY
    /
    "security_metrics.png"
)

print()

print(
    "Visualization test complete."
)

print("=" * 70)