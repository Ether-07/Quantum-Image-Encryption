import numpy as np

from src.encryption.block_transform import (
    create_local_permutation,
    permute_block,
    inverse_local_permutation
)


block = np.arange(
    64,
    dtype=np.uint8
).reshape(
    8,
    8
)


permutation = create_local_permutation(
    8,
    12345
)

permuted = permute_block(
    block,
    permutation
)

inverse = inverse_local_permutation(
    permutation
)

recovered = (
    permuted.flatten()[
        inverse
    ].reshape(
        8,
        8
    )
)


print("Original:")
print(block)

print("\nPermuted:")
print(permuted)

print("\nRecovered:")
print(recovered)

print(
    "\nRecovery successful:",
    np.array_equal(
        block,
        recovered
    )
)