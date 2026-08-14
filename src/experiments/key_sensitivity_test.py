from PIL import Image
import numpy as np

from src.encryption.pipeline import (
    encrypt_file
)

from src.analysis.differential import (
    calculate_npcr,
    calculate_uaci
)


input_path = (
    "images/test.png"
)

encrypted1_path = (
    "results/key1.png"
)

encrypted2_path = (
    "results/key2.png"
)


key1 = (
    "QuantumImageKey123"
)

key2 = (
    "QuantumImageKey124"
)


encrypt_file(
    input_path,
    encrypted1_path,
    key1
)

encrypt_file(
    input_path,
    encrypted2_path,
    key2
)


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


npcr = calculate_npcr(
    encrypted1,
    encrypted2
)

uaci = calculate_uaci(
    encrypted1,
    encrypted2
)


print("Key 1:")
print(key1)

print("\nKey 2:")
print(key2)

print(
    "\nNPCR between ciphertexts:"
)

print(
    f"{npcr:.6f}%"
)

print(
    "\nUACI between ciphertexts:"
)

print(
    f"{uaci:.6f}%"
)