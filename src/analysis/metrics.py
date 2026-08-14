import numpy as np

from src.analysis.entropy import (
    calculate_entropy
)

from src.analysis.correlation import (
    calculate_correlations
)

from src.analysis.differential import (
    calculate_npcr,
    calculate_uaci
)


def analyze_image(
    image
):
    """
    Calculate the main security-related
    metrics for a single grayscale image.
    """

    image = np.asarray(
        image,
        dtype=np.uint8
    )

    correlations = calculate_correlations(
        image
    )

    return {
        "entropy":
            calculate_entropy(image),

        "horizontal_correlation":
            correlations["horizontal"],

        "vertical_correlation":
            correlations["vertical"],

        "diagonal_correlation":
            correlations["diagonal"]
    }


def analyze_differential(
    image1,
    image2
):
    """
    Calculate differential metrics between
    two encrypted images.
    """

    return {
        "NPCR":
            calculate_npcr(
                image1,
                image2
            ),

        "UACI":
            calculate_uaci(
                image1,
                image2
            )
    }