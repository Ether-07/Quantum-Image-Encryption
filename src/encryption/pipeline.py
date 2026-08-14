import numpy as np

from src.image.preprocessing import (
    load_image,
    convert_to_grayscale,
    image_to_array,
    split_into_blocks
)

from src.image.reconstruction import (
    save_image
)

from src.encryption.key_generator import (
    derive_all_subkeys
)

from src.encryption.block_permutation import (
    create_block_permutation,
    apply_block_permutation
)

from src.encryption.block_transform import (
    create_local_permutation,
    permute_block,
    inverse_local_permutation
)

from src.encryption.quantum_keystream import (
    generate_quantum_bits,
    bits_to_bytes
)

from src.encryption.diffusion import (
    forward_diffusion,
    backward_diffusion,
    inverse_forward_diffusion,
    inverse_backward_diffusion
)


BLOCK_SIZE = 8


def bytes_to_seed(key_bytes):
    """
    Convert key material into a deterministic seed.
    """

    return int.from_bytes(
        key_bytes[:8],
        byteorder="big"
    )


def encrypt_array(
    image_array,
    key
):
    """
    Encrypt a grayscale image array.
    """

    height, width = image_array.shape

    if (
        height % BLOCK_SIZE != 0
        or
        width % BLOCK_SIZE != 0
    ):
        raise ValueError(
            "Image dimensions must be "
            "divisible by 8."
        )

    subkeys = derive_all_subkeys(
        key
    )

    # -----------------------------
    # 1. Split into blocks
    # -----------------------------

    blocks = split_into_blocks(
        image_array,
        BLOCK_SIZE
    )

    # -----------------------------
    # 2. Block permutation
    # -----------------------------

    block_permutation = (
        create_block_permutation(
            len(blocks),
            subkeys["block"]
        )
    )

    blocks = apply_block_permutation(
        blocks,
        block_permutation
    )

    # -----------------------------
    # 3. Local pixel permutation
    # -----------------------------

    pixel_seed = bytes_to_seed(
        subkeys["pixel"]
    )

    permuted_blocks = []

    for index, block in enumerate(
        blocks
    ):

        local_permutation = (
            create_local_permutation(
                BLOCK_SIZE,
                pixel_seed + index
            )
        )

        transformed = permute_block(
            block,
            local_permutation
        )

        permuted_blocks.append(
            transformed
        )

    # -----------------------------
    # 4. Flatten blocks
    # -----------------------------

    data = np.concatenate(
        [
            block.flatten()
            for block in permuted_blocks
        ]
    ).astype(
        np.uint8
    )

    # -----------------------------
    # 5. Quantum stream A
    # -----------------------------

    required_bits = (
        len(data) * 8
    )

    quantum_bits_1 = (
        generate_quantum_bits(
            key,
            required_bits
        )
    )

    quantum_stream_1 = np.asarray(
        bits_to_bytes(
            quantum_bits_1
        ),
        dtype=np.uint8
    )

    # -----------------------------
    # 6. Quantum stream B
    # -----------------------------

    quantum_bits_2 = (
        generate_quantum_bits(
            key + "::BACKWARD",
            required_bits
        )
    )

    quantum_stream_2 = np.asarray(
        bits_to_bytes(
            quantum_bits_2
        ),
        dtype=np.uint8
    )

    # -----------------------------
    # 7. Forward diffusion
    # -----------------------------

    forward = forward_diffusion(
        data,
        quantum_stream_1
    )

    # -----------------------------
    # 8. Backward diffusion
    # -----------------------------

    encrypted = backward_diffusion(
        forward,
        quantum_stream_2
    )

    return encrypted.reshape(
        height,
        width
    )


def decrypt_array(
    encrypted_array,
    key
):
    """
    Decrypt a grayscale image array.
    """

    height, width = encrypted_array.shape

    subkeys = derive_all_subkeys(
        key
    )

    encrypted = (
        encrypted_array
        .flatten()
        .astype(np.uint8)
    )

    required_bits = (
        len(encrypted) * 8
    )

    # -----------------------------
    # 1. Quantum stream A
    # -----------------------------

    quantum_bits_1 = (
        generate_quantum_bits(
            key,
            required_bits
        )
    )

    quantum_stream_1 = np.asarray(
        bits_to_bytes(
            quantum_bits_1
        ),
        dtype=np.uint8
    )

    # -----------------------------
    # 2. Quantum stream B
    # -----------------------------

    quantum_bits_2 = (
        generate_quantum_bits(
            key + "::BACKWARD",
            required_bits
        )
    )

    quantum_stream_2 = np.asarray(
        bits_to_bytes(
            quantum_bits_2
        ),
        dtype=np.uint8
    )

    # -----------------------------
    # 3. Reverse backward diffusion
    # -----------------------------

    forward = inverse_backward_diffusion(
        encrypted,
        quantum_stream_2
    )

    # -----------------------------
    # 4. Reverse forward diffusion
    # -----------------------------

    data = inverse_forward_diffusion(
        forward,
        quantum_stream_1
    )

    # -----------------------------
    # 5. Recreate blocks
    # -----------------------------

    number_of_blocks = (
        height // BLOCK_SIZE
    ) * (
        width // BLOCK_SIZE
    )

    block_length = (
        BLOCK_SIZE * BLOCK_SIZE
    )

    blocks = []

    for index in range(
        number_of_blocks
    ):

        start = (
            index * block_length
        )

        end = (
            start + block_length
        )

        block = data[
            start:end
        ].reshape(
            BLOCK_SIZE,
            BLOCK_SIZE
        )

        blocks.append(
            block
        )

    # -----------------------------
    # 6. Reverse local permutation
    # -----------------------------

    pixel_seed = bytes_to_seed(
        subkeys["pixel"]
    )

    restored_blocks = []

    for index, block in enumerate(
        blocks
    ):

        permutation = (
            create_local_permutation(
                BLOCK_SIZE,
                pixel_seed + index
            )
        )

        inverse = (
            inverse_local_permutation(
                permutation
            )
        )

        restored = (
            block.flatten()[
                inverse
            ].reshape(
                BLOCK_SIZE,
                BLOCK_SIZE
            )
        )

        restored_blocks.append(
            restored
        )

    # -----------------------------
    # 7. Reverse block permutation
    # -----------------------------

    permutation = (
        create_block_permutation(
            len(restored_blocks),
            subkeys["block"]
        )
    )

    original_blocks = [
        None
    ] * len(restored_blocks)

    # IMPORTANT:
    # permutation[index] is the
    # original block position.

    for index, block in enumerate(
        restored_blocks
    ):

        original_blocks[
            permutation[index]
        ] = block

    # -----------------------------
    # 8. Reconstruct image
    # -----------------------------

    image = np.zeros(
        (height, width),
        dtype=np.uint8
    )

    index = 0

    for row in range(
        0,
        height,
        BLOCK_SIZE
    ):

        for col in range(
            0,
            width,
            BLOCK_SIZE
        ):

            image[
                row:row + BLOCK_SIZE,
                col:col + BLOCK_SIZE
            ] = original_blocks[
                index
            ]

            index += 1

    return image


def encrypt_file(
    input_path,
    output_path,
    key
):
    """
    Encrypt an image file.
    """

    image = load_image(
        input_path
    )

    gray = convert_to_grayscale(
        image
    )

    pixels = image_to_array(
        gray
    )

    encrypted = encrypt_array(
        pixels,
        key
    )

    save_image(
        encrypted,
        output_path
    )


def decrypt_file(
    input_path,
    output_path,
    key
):
    """
    Decrypt an encrypted image file.
    """

    image = load_image(
        input_path
    )

    encrypted = image_to_array(
        image.convert("L")
    )

    decrypted = decrypt_array(
        encrypted,
        key
    )

    save_image(
        decrypted,
        output_path
    )