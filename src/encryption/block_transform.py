import numpy as np


def create_local_permutation(
    block_size,
    seed
):
    """
    Create a permutation for pixels
    inside one block.
    """

    rng = np.random.default_rng(
        seed
    )

    number_of_pixels = (
        block_size * block_size
    )

    return rng.permutation(
        number_of_pixels
    )


def permute_block(
    block,
    permutation
):
    """
    Apply a pixel permutation to a block.
    """

    flat = block.flatten()

    return flat[
        permutation
    ].reshape(
        block.shape
    )


def inverse_local_permutation(
    permutation
):
    """
    Create the inverse local permutation.
    """

    inverse = np.empty_like(
        permutation
    )

    inverse[permutation] = np.arange(
        len(permutation)
    )

    return inverse