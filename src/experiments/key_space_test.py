from src.analysis.key_space import (
    calculate_key_space,
    calculate_key_bits
)


# Example:
# 94 printable ASCII characters

character_set = 94

key_lengths = [
    8,
    12,
    16,
    20,
    32
]


for length in key_lengths:

    space = calculate_key_space(
        character_set,
        length
    )

    bits = calculate_key_bits(
        character_set,
        length
    )

    print(
        f"Key length: {length}"
    )

    print(
        f"Key space: {space}"
    )

    print(
        f"Theoretical entropy: "
        f"{bits:.2f} bits"
    )

    print(
        "-" * 40
    )