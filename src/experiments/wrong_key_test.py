from src.encryption.decrypt import (
    decrypt_image
)

from PIL import Image
import numpy as np


encrypted_path = (
    "results/encrypted.png"
)

output_path = (
    "results/wrong_key_decrypted.png"
)

wrong_key = "QuantumImageKey124"


decrypt_image(
    encrypted_path,
    output_path,
    wrong_key
)


original = np.asarray(
    Image.open(
        "images/test.png"
    ).convert("L"),
    dtype=np.uint8
)

wrong_decrypted = np.asarray(
    Image.open(
        output_path
    ).convert("L"),
    dtype=np.uint8
)


same = np.array_equal(
    original,
    wrong_decrypted
)


print("Wrong-key decryption successful:")
print(same)


difference = np.abs(
    original.astype(np.int16)
    -
    wrong_decrypted.astype(np.int16)
)


print("\nTotal absolute difference:")
print(difference.sum())