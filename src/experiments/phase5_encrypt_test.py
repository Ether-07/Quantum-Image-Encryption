from src.encryption.pipeline import (
    encrypt_file,
    decrypt_file
)


input_path = (
    "images/test.png"
)

encrypted_path = (
    "results/phase5_encrypted.png"
)

decrypted_path = (
    "results/phase5_decrypted.png"
)

key = "QuantumImageKey123"


print("Encrypting...")

encrypt_file(
    input_path,
    encrypted_path,
    key
)

print(
    "Encrypted:",
    encrypted_path
)


print("\nDecrypting...")

decrypt_file(
    encrypted_path,
    decrypted_path,
    key
)

print(
    "Decrypted:",
    decrypted_path
)