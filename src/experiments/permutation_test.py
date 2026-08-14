import numpy as np

from src.encryption.permutation import (
    create_permutation,
    apply_permutation,
    inverse_permutation
)


data = np.array(
    [10, 20, 30, 40, 50, 60, 70, 80],
    dtype=np.uint8
)

seed = 12345

permutation = create_permutation(
    len(data),
    seed
)

permuted = apply_permutation(
    data,
    permutation
)

inverse = inverse_permutation(
    permutation
)

recovered = apply_permutation(
    permuted,
    inverse
)


print("Original:")
print(data)

print("\nPermutation:")
print(permutation)

print("\nPermuted:")
print(permuted)

print("\nRecovered:")
print(recovered)

print(
    "\nRecovery successful:",
    np.array_equal(data, recovered)
)