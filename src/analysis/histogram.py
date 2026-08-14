import numpy as np
from PIL import Image


def calculate_histogram(image):
    """
    Calculate the frequency of each grayscale
    intensity value from 0 to 255.
    """

    if isinstance(image, Image.Image):
        image = image.convert("L")
        image = np.asarray(
            image,
            dtype=np.uint8
        )

    image = np.asarray(
        image,
        dtype=np.uint8
    )

    histogram = np.bincount(
        image.flatten(),
        minlength=256
    )

    return histogram


def histogram_uniformity_score(
    histogram
):
    """
    Calculate a simple histogram uniformity
    score using normalized variance.

    Lower variance indicates a more uniform
    histogram.
    """

    histogram = np.asarray(
        histogram,
        dtype=np.float64
    )

    expected = (
        histogram.sum() / 256.0
    )

    if expected == 0:
        return 0.0

    variance = np.mean(
        (
            histogram - expected
        ) ** 2
    )

    normalized_variance = (
        variance /
        (expected ** 2)
    )

    return normalized_variance