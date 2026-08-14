import numpy as np

from src.encryption.block_permutation import (
    create_block_permutation,
    apply_block_permutation
)


blocks = [
    np.array([[1, 1], [1, 1]]),
    np.array([[2, 2], [2, 2]]),
    np.array([[3, 3], [3, 3]]),
    np.array([[4, 4], [4, 4]])
]


key = b"12345678ABCDEFGH"


permutation = create_block_permutation(
    len(blocks),
    key
)

permuted = apply_block_permutation(
    blocks,
    permutation
)


recovered = [
    None
] * len(blocks)


for index, block in enumerate(
    permuted
):

    recovered[
        permutation[index]
    ] = block


print("Permutation:")
print(permutation)

print("\nOriginal block values:")
print([
    block[0, 0]
    for block in blocks
])

print("\nPermuted block values:")
print([
    block[0, 0]
    for block in permuted
])

print("\nRecovered block values:")
print([
    block[0, 0]
    for block in recovered
])

print(
    "\nRecovery successful:",
    all(
        np.array_equal(
            blocks[i],
            recovered[i]
        )
        for i in range(len(blocks))
    )
)