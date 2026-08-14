from PIL import Image
import numpy as np

from src.encryption.pipeline import (
    encrypt_file
)

from src.analysis.differential import (
    calculate_npcr,
    calculate_uaci
)


original_path = (
    "images/test.png"
)

modified_path = (
    "images/test_modified.png"
)

encrypted1_path = (
    "results/differential_1.png"
)

encrypted2_path = (
    "results/differential_2.png"
)


key = "QuantumImageKey123"


# -----------------------------------
# Load original
# -----------------------------------

image = Image.open(
    original_path
).convert("L")

image_array = np.asarray(
    image,
    dtype=np.uint8
).copy()


# -----------------------------------
# Modify ONE pixel
# -----------------------------------

modified_array = (
    image_array.copy()
)

old_value = int(
    modified_array[0, 0]
)

modified_array[0, 0] = (
    old_value + 1
) % 256


Image.fromarray(
    modified_array
).save(
    modified_path
)


print(
    "Changed pixel (0, 0):"
)

print(
    f"{old_value} -> "
    f"{modified_array[0, 0]}"
)


# -----------------------------------
# Encrypt both
# -----------------------------------

encrypt_file(
    original_path,
    encrypted1_path,
    key
)

encrypt_file(
    modified_path,
    encrypted2_path,
    key
)


# -----------------------------------
# Load ciphertexts
# -----------------------------------

encrypted1 = np.asarray(
    Image.open(
        encrypted1_path
    ).convert("L"),
    dtype=np.uint8
)

encrypted2 = np.asarray(
    Image.open(
        encrypted2_path
    ).convert("L"),
    dtype=np.uint8
)


# -----------------------------------
# Calculate metrics
# -----------------------------------

npcr = calculate_npcr(
    encrypted1,
    encrypted2
)

uaci = calculate_uaci(
    encrypted1,
    encrypted2
)


print(
    "\nNPCR:"
)

print(
    f"{npcr:.6f}%"
)


print(
    "\nUACI:"
)

print(
    f"{uaci:.6f}%"
)