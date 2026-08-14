import numpy as np

from src.encryption.diffusion import (
    xor_diffusion
)


data = np.array(
    [10, 20, 30, 40, 50],
    dtype=np.uint8
)

key = np.array(
    [100, 200, 50, 80, 10],
    dtype=np.uint8
)

encrypted = xor_diffusion(
    data,
    key
)

decrypted = xor_diffusion(
    encrypted,
    key
)


print("Original:")
print(data)

print("\nEncrypted:")
print(encrypted)

print("\nDecrypted:")
print(decrypted)

print(
    "\nRecovery successful:",
    np.array_equal(data, decrypted)
)