import numpy as np

from src.analysis.metrics import (
    analyze_image,
    analyze_differential
)

from src.analysis.key_space import (
    calculate_key_space,
    calculate_key_bits
)

from src.encryption.pipeline import (
    encrypt_array
)


def analyze_security(
    original_image,
    encrypted_image
):
    """
    Calculate security metrics for
    the original and encrypted images.
    """

    original_image = np.asarray(
        original_image,
        dtype=np.uint8
    )

    encrypted_image = np.asarray(
        encrypted_image,
        dtype=np.uint8
    )

    if original_image.shape != encrypted_image.shape:
        raise ValueError(
            "Original and encrypted images "
            "must have identical shapes."
        )

    original_metrics = analyze_image(
        original_image
    )

    encrypted_metrics = analyze_image(
        encrypted_image
    )

    return {
        "original": original_metrics,
        "encrypted": encrypted_metrics
    }


def analyze_key_sensitivity(
    original_image,
    key
):

    original_image = np.asarray(
        original_image,
        dtype=np.uint8
    )

    if not key:

        raise ValueError(
            "Encryption key cannot be empty."
        )

    last_character = key[-1]

    if last_character == "~":

        replacement = "!"

    else:

        replacement = chr(
            ord(last_character) + 1
        )

    modified_key = (
        key[:-1] + replacement
    )

    encrypted_1 = encrypt_array(
        original_image,
        key
    )

    encrypted_2 = encrypt_array(
        original_image,
        modified_key
    )

    differential = analyze_differential(
        encrypted_1,
        encrypted_2
    )

    return {
        "NPCR": differential["NPCR"],
        "UACI": differential["UACI"],
        "modified_key": modified_key
    }


def analyze_key_space(
    key
):
    """
    Calculate theoretical key-space
    information for the supplied key.

    The GUI uses printable ASCII characters
    as the character set.
    """

    if not key:
        raise ValueError(
            "Encryption key cannot be empty."
        )

    character_set_size = 95
    key_length = len(key)

    space = calculate_key_space(
        character_set_size,
        key_length
    )

    bits = calculate_key_bits(
        character_set_size,
        key_length
    )

    return {
        "character_set_size":
            character_set_size,

        "key_length":
            key_length,

        "key_space":
            space,

        "key_bits":
            bits
    }