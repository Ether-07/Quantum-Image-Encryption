def calculate_key_space(
    character_set_size,
    key_length
):
    """
    Calculate the theoretical number of
    possible strings.
    """

    if character_set_size <= 0:
        raise ValueError(
            "Character set size must be positive."
        )

    if key_length <= 0:
        raise ValueError(
            "Key length must be positive."
        )

    return character_set_size ** key_length


def calculate_key_bits(
    character_set_size,
    key_length
):
    """
    Calculate theoretical key-space size
    in bits.
    """

    import math

    return (
        key_length
        *
        math.log2(
            character_set_size
        )
    )