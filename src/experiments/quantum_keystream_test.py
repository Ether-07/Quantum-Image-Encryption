from src.encryption.quantum_keystream import (
    generate_quantum_bits
)


key = "QuantumImageKey123"

bits = generate_quantum_bits(
    key,
    32
)

print("Generated bits:")
print(bits)

print("\nNumber of bits:")
print(len(bits))