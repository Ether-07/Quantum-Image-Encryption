from src.encryption.quantum_keystream import (
    bits_to_bytes
)


bits = [
    1, 0, 1, 0,
    1, 1, 0, 1
]

result = bits_to_bytes(bits)

print("Bits:")
print(bits)

print("\nConverted byte:")
print(result)