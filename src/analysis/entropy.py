import numpy as np


def calculate_entropy(image):
    """
    Calculate Shannon entropy of an 8-bit image.
    """

    image = np.asarray(
        image,
        dtype=np.uint8
    )

    histogram = np.bincount(
        image.flatten(),
        minlength=256
    )

    probabilities = (
        histogram /
        histogram.sum()
    )

    probabilities = probabilities[
        probabilities > 0
    ]

    entropy = -np.sum(
        probabilities
        *
        np.log2(probabilities)
    )

    return float(entropy)