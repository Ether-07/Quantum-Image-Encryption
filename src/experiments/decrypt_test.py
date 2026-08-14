from src.encryption.decrypt import (
    decrypt_image
)


encrypted_path = (
    "results/encrypted.png"
)

output_path = (
    "results/decrypted.png"
)

key = "QuantumImageKey123"


decrypt_image(
    encrypted_path,
    output_path,
    key
)


print("Decryption completed.")

print("\nDecrypted image:")
print(output_path)