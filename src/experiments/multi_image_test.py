from src.encryption.pipeline import (
    encrypt_file,
    decrypt_file
)

from PIL import Image
import numpy as np


tests = [
    (
        "images/test.png",
        "results/test1_enc.png",
        "results/test1_dec.png"
    ),
    (
        "images/test2.png",
        "results/test2_enc.png",
        "results/test2_dec.png"
    )
]


key = "QuantumImageKey123"


for (
    original_path,
    encrypted_path,
    decrypted_path
) in tests:

    print(
        f"\nTesting: {original_path}"
    )

    encrypt_file(
        original_path,
        encrypted_path,
        key
    )

    decrypt_file(
        encrypted_path,
        decrypted_path,
        key
    )

    original = np.asarray(
        Image.open(
            original_path
        ).convert("L"),
        dtype=np.uint8
    )

    decrypted = np.asarray(
        Image.open(
            decrypted_path
        ).convert("L"),
        dtype=np.uint8
    )

    print(
        "Recovery:",
        np.array_equal(
            original,
            decrypted
        )
    )