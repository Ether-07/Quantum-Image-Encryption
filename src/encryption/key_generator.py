import hashlib


def derive_key_material(user_key):
    """
    Derive 32 bytes of master key material.
    """

    if not isinstance(user_key, str):
        raise TypeError(
            "Key must be a string."
        )

    if len(user_key) < 8:
        raise ValueError(
            "Key must contain at least 8 characters."
        )

    return hashlib.sha256(
        user_key.encode("utf-8")
    ).digest()


def derive_subkey(
    master_key,
    purpose
):
    """
    Derive a deterministic subkey for
    a specific encryption component.
    """

    if not isinstance(
        master_key,
        bytes
    ):
        raise TypeError(
            "master_key must be bytes."
        )

    data = (
        purpose.encode("utf-8")
        +
        master_key
    )

    return hashlib.sha256(
        data
    ).digest()


def derive_all_subkeys(user_key):
    """
    Generate separate subkeys for
    each encryption component.
    """

    master_key = derive_key_material(
        user_key
    )

    return {
        "master": master_key,

        "block": derive_subkey(
            master_key,
            "BLOCK-PERMUTATION"
        ),

        "pixel": derive_subkey(
            master_key,
            "PIXEL-PERMUTATION"
        ),

        "quantum": derive_subkey(
            master_key,
            "QUANTUM-CIRCUIT"
        ),

        "forward": derive_subkey(
            master_key,
            "FORWARD-DIFFUSION"
        ),

        "backward": derive_subkey(
            master_key,
            "BACKWARD-DIFFUSION"
        )
    }