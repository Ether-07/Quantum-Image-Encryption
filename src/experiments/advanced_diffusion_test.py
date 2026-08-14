import numpy as np

from src.encryption.diffusion import (
    forward_diffusion,
    inverse_forward_diffusion,
    backward_diffusion,
    inverse_backward_diffusion
)


data = np.array(
    [10, 20, 30, 40, 50, 60],
    dtype=np.uint8
)

key1 = np.array(
    [1, 2, 3, 4, 5, 6],
    dtype=np.uint8
)

key2 = np.array(
    [100, 110, 120, 130, 140, 150],
    dtype=np.uint8
)


forward = forward_diffusion(
    data,
    key1
)

recovered_forward = (
    inverse_forward_diffusion(
        forward,
        key1
    )
)


backward = backward_diffusion(
    data,
    key2
)

recovered_backward = (
    inverse_backward_diffusion(
        backward,
        key2
    )
)


print("Original:")
print(data)

print("\nForward result:")
print(forward)

print("\nForward recovered:")
print(recovered_forward)

print(
    "Forward recovery:",
    np.array_equal(
        data,
        recovered_forward
    )
)

print("\nBackward result:")
print(backward)

print("\nBackward recovered:")
print(recovered_backward)

print(
    "Backward recovery:",
    np.array_equal(
        data,
        recovered_backward
    )
)