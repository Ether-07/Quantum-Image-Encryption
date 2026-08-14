import numpy as np


def bytes_to_seed(key_bytes):
    """
    Convert key bytes into a deterministic integer seed.
    """

    return int.from_bytes(
        key_bytes[:8],
        byteorder="big"
    )


def create_block_permutation(
    number_of_blocks,
    key_bytes
):
    """
    Create a deterministic block permutation.
    """

    seed = bytes_to_seed(
        key_bytes
    )

    rng = np.random.default_rng(
        seed
    )

    return rng.permutation(
        number_of_blocks
    )


def apply_block_permutation(
    blocks,
    permutation
):
    """
    Reorder image blocks.
    """

    return [
        blocks[index].copy()
        for index in permutation
    ]


def invert_block_permutation(
    permutation
):
    """
    Create the mathematical inverse
    of a permutation.
    """

    inverse = np.empty_like(
        permutation
    )

    inverse[permutation] = np.arange(
        len(permutation)
    )

    return inverse