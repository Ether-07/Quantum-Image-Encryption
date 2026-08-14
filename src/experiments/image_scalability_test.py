import time
import os

from src.encryption.pipeline import (
    encrypt_file,
    decrypt_file
)


TESTS = [
    (
        "images/test.png",
        "128x128"
    ),
    (
        "images/test_256.png",
        "256x256"
    ),
    (
        "images/test_512.png",
        "512x512"
    )
]


KEY = "QuantumImageKey123"


print("=" * 70)
print("PHASE 7 - IMAGE SIZE SCALABILITY")
print("=" * 70)


for input_path, label in TESTS:

    print("\n" + "=" * 70)

    print(
        f"Testing image: {label}"
    )

    if not os.path.exists(input_path):

        print(
            f"SKIPPED - file not found: "
            f"{input_path}"
        )

        continue


    encrypted_path = (
        f"results/"
        f"scalability_{label}_enc.png"
    )

    decrypted_path = (
        f"results/"
        f"scalability_{label}_dec.png"
    )


    # -----------------------------------------
    # Encryption
    # -----------------------------------------

    start = time.perf_counter()

    encrypt_file(
        input_path,
        encrypted_path,
        KEY
    )

    encryption_time = (
        time.perf_counter()
        - start
    )


    # -----------------------------------------
    # Decryption
    # -----------------------------------------

    start = time.perf_counter()

    decrypt_file(
        encrypted_path,
        decrypted_path,
        KEY
    )

    decryption_time = (
        time.perf_counter()
        - start
    )


    print(
        f"Encryption : "
        f"{encryption_time:.6f} sec"
    )

    print(
        f"Decryption : "
        f"{decryption_time:.6f} sec"
    )

    print(
        f"Total      : "
        f"{encryption_time + decryption_time:.6f} sec"
    )


print("\n" + "=" * 70)
print("SCALABILITY TEST COMPLETE")
print("=" * 70)