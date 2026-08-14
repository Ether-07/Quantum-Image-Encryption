from src.encryption.encrypt import (
    encrypt_image
)


input_path = "images/test.png"

output_path = "results/encrypted.png"

key = "QuantumImageKey123"


metadata = encrypt_image(
    input_path,
    output_path,
    key
)


print("Encryption completed.")

print("\nEncrypted image:")
print(output_path)

print("\nOriginal shape:")
print(metadata["original_shape"])