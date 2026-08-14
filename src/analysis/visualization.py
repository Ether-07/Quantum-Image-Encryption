import matplotlib.pyplot as plt
import numpy as np


def plot_histograms(
    original_histogram,
    encrypted_histogram,
    output_path
):
    """
    Plot original and encrypted image
    histograms.
    """

    x = np.arange(256)

    plt.figure(
        figsize=(10, 5)
    )

    plt.plot(
        x,
        original_histogram,
        label="Original"
    )

    plt.plot(
        x,
        encrypted_histogram,
        label="Encrypted"
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

    plt.legend()

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300
    )

    plt.close()


def plot_metric_comparison(
    metric_names,
    values,
    title,
    output_path
):
    """
    Plot a simple metric comparison.
    """

    plt.figure(
        figsize=(10, 5)
    )

    positions = np.arange(
        len(metric_names)
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

    plt.title(
        title
    )

    plt.tight_layout()

    plt.savefig(
        output_path,
        dpi=300
    )

    plt.close()