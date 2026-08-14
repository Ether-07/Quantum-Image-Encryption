import numpy as np


def _correlation(
    x,
    y
):
    """
    Calculate Pearson correlation coefficient.
    """

    x = np.asarray(
        x,
        dtype=np.float64
    )

    y = np.asarray(
        y,
        dtype=np.float64
    )

    if len(x) < 2:
        return 0.0

    x_mean = x.mean()
    y_mean = y.mean()

    numerator = np.sum(
        (x - x_mean)
        *
        (y - y_mean)
    )

    denominator = np.sqrt(
        np.sum(
            (x - x_mean) ** 2
        )
        *
        np.sum(
            (y - y_mean) ** 2
        )
    )

    if denominator == 0:
        return 0.0

    return float(
        numerator / denominator
    )


def horizontal_correlation(
    image
):
    """
    Correlation between horizontally
    adjacent pixels.
    """

    image = np.asarray(
        image,
        dtype=np.uint8
    )

    x = image[:, :-1].flatten()
    y = image[:, 1:].flatten()

    return _correlation(
        x,
        y
    )


def vertical_correlation(
    image
):
    """
    Correlation between vertically
    adjacent pixels.
    """

    image = np.asarray(
        image,
        dtype=np.uint8
    )

    x = image[:-1, :].flatten()
    y = image[1:, :].flatten()

    return _correlation(
        x,
        y
    )


def diagonal_correlation(
    image
):
    """
    Correlation between diagonally
    adjacent pixels.
    """

    image = np.asarray(
        image,
        dtype=np.uint8
    )

    x = image[:-1, :-1].flatten()
    y = image[1:, 1:].flatten()

    return _correlation(
        x,
        y
    )


def calculate_correlations(
    image
):
    """
    Calculate horizontal, vertical,
    and diagonal correlations.
    """

    return {
        "horizontal":
            horizontal_correlation(image),

        "vertical":
            vertical_correlation(image),

        "diagonal":
            diagonal_correlation(image)
    }