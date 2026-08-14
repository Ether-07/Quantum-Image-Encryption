import time
import os

from src.encryption.pipeline import (
    encrypt_file,
    decrypt_file
)


INPUT_PATH = "images/test.png"

ENCRYPTED_PATH = (
    "results/phase7_encrypted.png"
)

DECRYPTED_PATH = (
    "results/phase7_decrypted.png"
)

KEY = "QuantumImageKey123"


print("=" * 70)
print("PHASE 7 - FULL ENCRYPTION PERFORMANCE")
print("=" * 70)


# --------------------------------------------------
# Check input
# --------------------------------------------------

if not os.path.exists(INPUT_PATH):

    raise FileNotFoundError(
        f"Input image not found: {INPUT_PATH}"
    )


# --------------------------------------------------
# Encryption
# --------------------------------------------------

print("\nEncrypting...")

start = time.perf_counter()

encrypt_file(
    INPUT_PATH,
    ENCRYPTED_PATH,
    KEY
)

encryption_time = (
    time.perf_counter()
    - start
)


print(
    "Encryption complete."
)


# --------------------------------------------------
# Decryption
# --------------------------------------------------

print("\nDecrypting...")

start = time.perf_counter()

decrypt_file(
    ENCRYPTED_PATH,
    DECRYPTED_PATH,
    KEY
)

decryption_time = (
    time.perf_counter()
    - start
)


print(
    "Decryption complete."
)


# --------------------------------------------------
# Results
# --------------------------------------------------

total_time = (
    encryption_time
    + decryption_time
)


print("\n" + "-" * 70)

print(
    f"Encryption time : "
    f"{encryption_time:.6f} seconds"
)

print(
    f"Decryption time : "
    f"{decryption_time:.6f} seconds"
)

print(
    f"Total time      : "
    f"{total_time:.6f} seconds"
)

print("-" * 70)