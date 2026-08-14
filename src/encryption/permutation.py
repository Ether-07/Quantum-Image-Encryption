import numpy as np


def create_permutation(length, seed):
    """
    Create a deterministic permutation.
    """

    rng = np.random.default_rng(seed)

    return rng.permutation(length)


def apply_permutation(data, permutation):
    """
    Apply a permutation to one-dimensional data.
    """

    data = np.asarray(data)

    return data[permutation]


def inverse_permutation(permutation):
    """
    Calculate the inverse of a permutation.
    """

    inverse = np.empty_like(permutation)

    inverse[permutation] = np.arange(
        len(permutation)
    )

    return inverse