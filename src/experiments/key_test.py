from src.encryption.key_generator import derive_key_material


key = "QuantumImageKey123"

material = derive_key_material(key)

print("Original key:")
print(key)

print("\nDerived key material:")
print(material)

print("\nKey material length:")
print(len(material), "bytes")

print("\nKey material in hexadecimal:")
print(material.hex())