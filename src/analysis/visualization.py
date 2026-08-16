import matplotlib.pyplot as plt
import numpy as np


# ============================================================
# HISTOGRAM COMPARISON
# ============================================================

def plot_histograms(
    original_histogram,
    encrypted_histogram,
    output_path
):
    """
    Plot original and encrypted image histograms.
    """

    original_histogram = np.asarray(
        original_histogram,
        dtype=np.float64
    )

    encrypted_histogram = np.asarray(
        encrypted_histogram,
        dtype=np.float64
    )

    x = np.arange(
        256
    )

    plt.figure(
        figsize=(10, 5)
    )

    plt.plot(
        x,
        original_histogram,
        label="Original",
        linewidth=1.2
    )

    plt.plot(
        x,
        encrypted_histogram,
        label="Encrypted",
        linewidth=1.2
    )

    plt.xlabel(
        "Pixel Intensity"
    )

    plt.ylabel(
        "Frequency"
    )

    plt.title(
        "Original vs Encrypted Histogram"
    )

    plt.xlim(
        0,
        255
    )

    plt.grid(
        alpha=0.2
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight"
    )

    plt.close()


# ============================================================
# CORRELATION COMPARISON
# ============================================================

def plot_correlation_comparison(
    original_correlations,
    encrypted_correlations,
    output_path
):
    """
    Compare horizontal, vertical, and diagonal
    pixel correlations between original and
    encrypted images.
    """

    names = [
        "Horizontal",
        "Vertical",
        "Diagonal"
    ]

    original_values = [
        original_correlations["horizontal"],
        original_correlations["vertical"],
        original_correlations["diagonal"]
    ]

    encrypted_values = [
        encrypted_correlations["horizontal"],
        encrypted_correlations["vertical"],
        encrypted_correlations["diagonal"]
    ]

    positions = np.arange(
        len(names)
    )

    width = 0.35

    plt.figure(
        figsize=(10, 5)
    )

    plt.bar(
        positions - width / 2,
        original_values,
        width,
        label="Original"
    )

    plt.bar(
        positions + width / 2,
        encrypted_values,
        width,
        label="Encrypted"
    )

    plt.axhline(
        0,
        linewidth=0.8
    )

    plt.xticks(
        positions,
        names
    )

    plt.ylabel(
        "Correlation Coefficient"
    )

    plt.title(
        "Pixel Correlation Comparison"
    )

    plt.ylim(
        -1.0,
        1.0
    )

    plt.grid(
        axis="y",
        alpha=0.2
    )

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight"
    )

    plt.close()


# ============================================================
# SECURITY METRICS
# ============================================================

def plot_security_metrics(
    entropy,
    npcr,
    uaci,
    output_path
):
    """
    Plot major security metrics.

    Entropy is normalized to a percentage of
    the ideal 8-bit entropy for visualization.
    """

    entropy_percentage = (
        entropy / 8.0
    ) * 100.0

    metric_names = [
        "Entropy\n(% of 8)",
        "NPCR",
        "UACI"
    ]

    values = [
        entropy_percentage,
        npcr,
        uaci
    ]

    positions = np.arange(
        len(metric_names)
    )

    plt.figure(
        figsize=(9, 5)
    )

    bars = plt.bar(
        positions,
        values
    )

    plt.xticks(
        positions,
        metric_names
    )

    plt.ylabel(
        "Percentage"
    )

    plt.title(
        "Security Metrics"
    )

    plt.ylim(
        0,
        105
    )

    plt.grid(
        axis="y",
        alpha=0.2
    )

    for bar, value in zip(
        bars,
        values
    ):

        plt.text(
            bar.get_x()
            +
            bar.get_width() / 2,
            value + 1,
            f"{value:.2f}%",
            ha="center",
            va="bottom"
        )

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight"
    )

    plt.close()


# ============================================================
# QUANTUM PERFORMANCE
# ============================================================

def plot_quantum_performance(
    bit_sizes,
    execution_times,
    output_path
):
    """
    Plot quantum keystream generation time
    against requested bit count.
    """

    bit_sizes = np.asarray(
        bit_sizes,
        dtype=np.float64
    )

    execution_times = np.asarray(
        execution_times,
        dtype=np.float64
    )

    plt.figure(
        figsize=(9, 5)
    )

    plt.plot(
        bit_sizes,
        execution_times,
        marker="o"
    )

    plt.xlabel(
        "Requested Quantum Bits"
    )

    plt.ylabel(
        "Generation Time (seconds)"
    )

    plt.title(
        "Quantum Keystream Generation Performance"
    )

    plt.grid(
        alpha=0.2
    )

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight"
    )

    plt.close()


# ============================================================
# GENERIC METRIC COMPARISON
# ============================================================

def plot_metric_comparison(
    metric_names,
    values,
    title,
    output_path
):
    """
    Plot a simple metric comparison.
    """

    positions = np.arange(
        len(metric_names)
    )

    plt.figure(
        figsize=(10, 5)
    )

    plt.bar(
        positions,
        values
    )

    plt.xticks(
        positions,
        metric_names,
        rotation=30
    )

    plt.ylabel(
        "Value"
    )

    plt.title(
        title
    )

    plt.grid(
        axis="y",
        alpha=0.2
    )

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=200,
        bbox_inches="tight"
    )

    plt.close()