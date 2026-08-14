import numpy as np
from PIL import Image

from src.encryption.key_generator import (
    derive_key_material
)

from src.encryption.permutation import (
    create_permutation,
    inverse_permutation
)

from src.encryption.quantum_keystream import (
    generate_quantum_bits,
    bits_to_bytes
)

from src.encryption.diffusion import (
    xor_diffusion
)

from src.image.reconstruction import (
    save_image
)


def decrypt_image(
    encrypted_path,
    output_path,
    key
):
    """
    Decrypt an image produced by encrypt_image().
    """

    # -----------------------------
    # 1. Load encrypted image
    # -----------------------------

    encrypted_image = Image.open(
        encrypted_path
    ).convert("L")

    encrypted_pixels = np.asarray(
        encrypted_image,
        dtype=np.uint8
    )

    original_shape = (
        encrypted_pixels.shape
    )

    encrypted_flat = (
        encrypted_pixels.flatten()
    )

    # -----------------------------
    # 2. Recreate key material
    # -----------------------------

    key_material = derive_key_material(
        key
    )

    seed = int.from_bytes(
        key_material[:8],
        byteorder="big"
    )

    # -----------------------------
    # 3. Recreate permutation
    # -----------------------------

    permutation = create_permutation(
        len(encrypted_flat),
        seed
    )

    # -----------------------------
    # 4. Recreate quantum keystream
    # -----------------------------

    required_bits = (
        len(encrypted_flat) * 8
    )

    quantum_bits = generate_quantum_bits(
        key,
        required_bits
    )

    quantum_bytes = bits_to_bytes(
        quantum_bits
    )

    quantum_bytes = np.asarray(
        quantum_bytes,
        dtype=np.uint8
    )

    # -----------------------------
    # 5. Reverse XOR
    # -----------------------------

    permuted = xor_diffusion(
        encrypted_flat,
        quantum_bytes
    )

    # -----------------------------
    # 6. Reverse permutation
    # -----------------------------

    inverse = inverse_permutation(
        permutation
    )

    original_flat = (
        permuted[inverse]
    )

    # -----------------------------
    # 7. Restore image shape
    # -----------------------------

    original_pixels = (
        original_flat.reshape(
            original_shape
        )
    )

    # -----------------------------
    # 8. Save decrypted image
    # -----------------------------

    save_image(
        original_pixels,
        output_path
    )