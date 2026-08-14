import numpy as np

from src.encryption.pipeline import (
    encrypt_array
)


valid_image = np.zeros(
    (128, 128),
    dtype=np.uint8
)

invalid_image = np.zeros(
    (130, 130),
    dtype=np.uint8
)


print("Testing 128 × 128 image:")

try:

    encrypt_array(
        valid_image,
        "QuantumImageKey123"
    )

    print("Accepted")

except Exception as error:

    print("Rejected:", error)


print("\nTesting 130 × 130 image:")

try:

    encrypt_array(
        invalid_image,
        "QuantumImageKey123"
    )

    print("Accepted")

except Exception as error:

    print("Rejected:", error)