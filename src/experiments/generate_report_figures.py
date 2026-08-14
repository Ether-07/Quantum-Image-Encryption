import os

import matplotlib.pyplot as plt
import numpy as np


OUTPUT_DIR = "docs/figures"


def ensure_output_directory():
    os.makedirs(OUTPUT_DIR, exist_ok=True)


def save_figure(filename):
    output_path = os.path.join(OUTPUT_DIR, filename)

    plt.tight_layout()
    plt.savefig(
        output_path,
        dpi=300,
        bbox_inches="tight"
    )
    plt.close()

    print(f"Generated: {output_path}")


def generate_entropy_figure():
    labels = [
        "Original",
        "Encrypted"
    ]

    values = [
        6.908056,
        7.988329
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(
        labels,
        values
    )

    plt.ylabel("Entropy (bits)")
    plt.title("Entropy Comparison")

    plt.ylim(0, 8.2)

    save_figure(
        "entropy_comparison.png"
    )


def generate_correlation_figure():
    directions = [
        "Horizontal",
        "Vertical",
        "Diagonal"
    ]

    original = [
        0.970758,
        0.951356,
        0.934675
    ]

    encrypted = [
        0.000958,
        0.007067,
        -0.000085
    ]

    x = np.arange(
        len(directions)
    )

    width = 0.35

    plt.figure(figsize=(9, 5))

    plt.bar(
        x - width / 2,
        original,
        width,
        label="Original"
    )

    plt.bar(
        x + width / 2,
        encrypted,
        width,
        label="Encrypted"
    )

    plt.xticks(
        x,
        directions
    )

    plt.ylabel("Correlation coefficient")
    plt.title("Pixel Correlation Comparison")
    plt.legend()

    plt.axhline(
        0,
        linewidth=0.8
    )

    save_figure(
        "correlation_comparison.png"
    )


def generate_npcr_uaci_figure():
    metrics = [
        "NPCR",
        "UACI"
    ]

    values = [
        99.707031,
        33.590519
    ]

    plt.figure(figsize=(8, 5))

    plt.bar(
        metrics,
        values
    )

    plt.ylabel("Percentage (%)")
    plt.title("NPCR and UACI")

    save_figure(
        "npcr_uaci.png"
    )


def generate_quantum_performance_figure():
    bits = [
        128,
        512,
        1024,
        4096,
        8192
    ]

    time_seconds = [
        0.020762,
        0.045600,
        0.084818,
        0.361393,
        0.726578
    ]

    throughput = [
        6165.08,
        11228.17,
        12072.85,
        11333.92,
        11274.77
    ]

    plt.figure(figsize=(9, 5))

    plt.plot(
        bits,
        throughput,
        marker="o"
    )

    plt.xlabel(
        "Requested bits"
    )

    plt.ylabel(
        "Throughput (bits/sec)"
    )

    plt.title(
        "Quantum Keystream Generation Throughput"
    )

    save_figure(
        "quantum_performance.png"
    )


def generate_scalability_figure():
    labels = [
        "128×128",
        "256×256",
        "512×512"
    ]

    times = [
        50.790058,
        217.319936,
        1914.999096
    ]

    plt.figure(figsize=(9, 5))

    plt.plot(
        labels,
        times,
        marker="o"
    )

    plt.xlabel(
        "Image Size"
    )

    plt.ylabel(
        "Total Execution Time (seconds)"
    )

    plt.title(
        "Image Scalability"
    )

    save_figure(
        "performance_scalability.png"
    )


def generate_noise_sweep_figure():
    noise_levels = [
        0.1,
        0.5,
        1,
        2,
        5
    ]

    tvd = [
        0.003,
        0.008,
        0.023,
        0.039,
        0.117
    ]

    plt.figure(figsize=(9, 5))

    plt.plot(
        noise_levels,
        tvd,
        marker="o"
    )

    plt.xlabel(
        "Noise Level (%)"
    )

    plt.ylabel(
        "Total Variation Distance"
    )

    plt.title(
        "Quantum Noise Sweep"
    )

    save_figure(
        "noise_sweep.png"
    )


def generate_noise_impact_figure():
    noise_levels = [
        0.1,
        0.5,
        1,
        2,
        5
    ]

    tvd = [
        0.003,
        0.008,
        0.023,
        0.039,
        0.117
    ]

    plt.figure(figsize=(9, 5))

    plt.bar(
        [
            "0.1%",
            "0.5%",
            "1%",
            "2%",
            "5%"
        ],
        tvd
    )

    plt.xlabel(
        "Noise Level"
    )

    plt.ylabel(
        "Total Variation Distance"
    )

    plt.title(
        "Impact of Quantum Noise"
    )

    save_figure(
        "noise_impact.png"
    )


def main():
    print("=" * 70)
    print("FINAL REPORT FIGURE GENERATION")
    print("=" * 70)

    ensure_output_directory()

    generate_entropy_figure()
    generate_correlation_figure()
    generate_npcr_uaci_figure()
    generate_quantum_performance_figure()
    generate_scalability_figure()
    generate_noise_sweep_figure()
    generate_noise_impact_figure()

    print("=" * 70)
    print("FIGURE GENERATION COMPLETE")
    print("=" * 70)


if __name__ == "__main__":
    main()