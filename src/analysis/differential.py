import numpy as np


def calculate_npcr(
    encrypted1,
    encrypted2
):
    """
    Calculate Number of Pixels Change Rate.
    """

    encrypted1 = np.asarray(
        encrypted1,
        dtype=np.uint8
    )

    encrypted2 = np.asarray(
        encrypted2,
        dtype=np.uint8
    )

    if encrypted1.shape != encrypted2.shape:
        raise ValueError(
            "Images must have identical shapes."
        )

    changed = np.count_nonzero(
        encrypted1 != encrypted2
    )

    total = encrypted1.size

    return (
        changed / total
    ) * 100.0


def calculate_uaci(
    encrypted1,
    encrypted2
):
    """
    Calculate Unified Average Changing
    Intensity.
    """

    encrypted1 = np.asarray(
        encrypted1,
        dtype=np.float64
    )

    encrypted2 = np.asarray(
        encrypted2,
        dtype=np.float64
    )

    if encrypted1.shape != encrypted2.shape:
        raise ValueError(
            "Images must have identical shapes."
        )

    difference = np.abs(
        encrypted1 - encrypted2
    )

    uaci = (
        difference.mean()
        /
        255.0
    ) * 100.0

    return float(uaci)