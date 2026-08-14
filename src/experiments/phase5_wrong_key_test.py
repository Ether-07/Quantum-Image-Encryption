from src.encryption.pipeline import (
    decrypt_file
)

from PIL import Image
import numpy as np


encrypted_path = (
    "results/phase5_encrypted.png"
)

wrong_output = (
    "results/phase5_wrong_key.png"
)

wrong_key = (
    "CompletelyWrongKey123"
)


decrypt_file(
    encrypted_path,
    wrong_output,
    wrong_key
)


original = np.asarray(
    Image.open(
        "images/test.png"
    ).convert("L"),
    dtype=np.uint8
)

wrong = np.asarray(
    Image.open(
        wrong_output
    ).convert("L"),
    dtype=np.uint8
)


same = np.array_equal(
    original,
    wrong
)


print(
    "Wrong key recovered original:"
)

print(same)


difference = np.abs(
    original.astype(np.int16)
    -
    wrong.astype(np.int16)
)


print(
    "\nTotal absolute difference:"
)

print(
    difference.sum()
)