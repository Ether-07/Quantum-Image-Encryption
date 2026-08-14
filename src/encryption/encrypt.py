import numpy as np

from src.image.preprocessing import (
    load_image,
    convert_to_grayscale,
    image_to_array
)

from src.encryption.key_generator import (
    derive_key_material
)

from src.encryption.permutation import (
    create_permutation
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


def encrypt_image(
    input_path,
    output_path,
    key
):
    """
    Encrypt an image using the
    prototype quantum-inspired pipeline.
    """

    # -----------------------------
    # 1. Load image
    # -----------------------------

    image = load_image(
        input_path
    )

    # -----------------------------
    # 2. Convert to grayscale
    # -----------------------------

    gray = convert_to_grayscale(
        image
    )

    # -----------------------------
    # 3. Convert to NumPy array
    # -----------------------------

    pixels = image_to_array(
        gray
    )

    original_shape = pixels.shape

    # -----------------------------
    # 4. Flatten image
    # -----------------------------

    flat = pixels.flatten()

    # -----------------------------
    # 5. Generate permutation seed
    # -----------------------------

    key_material = derive_key_material(
        key
    )

    seed = int.from_bytes(
        key_material[:8],
        byteorder="big"
    )

    # -----------------------------
    # 6. Permute pixels
    # -----------------------------

    permutation = create_permutation(
        len(flat),
        seed
    )

    permuted = flat[
        permutation
    ]

    # -----------------------------
    # 7. Generate quantum bits
    # -----------------------------

    required_bits = (
        len(permuted) * 8
    )

    quantum_bits = generate_quantum_bits(
        key,
        required_bits
    )

    # -----------------------------
    # 8. Convert bits to bytes
    # -----------------------------

    quantum_bytes = bits_to_bytes(
        quantum_bits
    )

    quantum_bytes = np.asarray(
        quantum_bytes,
        dtype=np.uint8
    )

    # -----------------------------
    # 9. XOR diffusion
    # -----------------------------

    encrypted_flat = xor_diffusion(
        permuted,
        quantum_bytes
    )

    # -----------------------------
    # 10. Restore image shape
    # -----------------------------

    encrypted_pixels = (
        encrypted_flat.reshape(
            original_shape
        )
    )

    # -----------------------------
    # 11. Save encrypted image
    # -----------------------------

    save_image(
        encrypted_pixels,
        output_path
    )

    return {
        "original_shape": original_shape,
        "permutation": permutation
    }