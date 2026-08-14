import numpy as np


MODULUS = 256
FEEDBACK_MULTIPLIER = 3


def forward_diffusion(
    data,
    keystream
):
    """
    Forward modular diffusion.

    C[0] = (P[0] + K[0]) mod 256

    C[i] = (
        P[i]
        + K[i]
        + 3 * C[i-1]
    ) mod 256
    """

    data = np.asarray(
        data,
        dtype=np.uint16
    )

    keystream = np.asarray(
        keystream,
        dtype=np.uint16
    )

    if data.shape != keystream.shape:
        raise ValueError(
            "Data and keystream must have "
            "the same shape."
        )

    if len(data) == 0:
        return np.array(
            [],
            dtype=np.uint8
        )

    result = np.empty(
        len(data),
        dtype=np.uint16
    )

    # First element
    result[0] = (
        int(data[0])
        + int(keystream[0])
    ) % MODULUS

    # Remaining elements
    for i in range(
        1,
        len(data)
    ):

        result[i] = (
            int(data[i])
            + int(keystream[i])
            + FEEDBACK_MULTIPLIER
            * int(result[i - 1])
        ) % MODULUS

    return result.astype(
        np.uint8
    )


def inverse_forward_diffusion(
    data,
    keystream
):
    """
    Reverse forward modular diffusion.

    P[0] = (C[0] - K[0]) mod 256

    P[i] = (
        C[i]
        - K[i]
        - 3 * C[i-1]
    ) mod 256
    """

    data = np.asarray(
        data,
        dtype=np.uint16
    )

    keystream = np.asarray(
        keystream,
        dtype=np.uint16
    )

    if data.shape != keystream.shape:
        raise ValueError(
            "Data and keystream must have "
            "the same shape."
        )

    if len(data) == 0:
        return np.array(
            [],
            dtype=np.uint8
        )

    result = np.empty(
        len(data),
        dtype=np.uint16
    )

    # First element
    result[0] = (
        int(data[0])
        - int(keystream[0])
    ) % MODULUS

    # Remaining elements
    for i in range(
        1,
        len(data)
    ):

        result[i] = (
            int(data[i])
            - int(keystream[i])
            - FEEDBACK_MULTIPLIER
            * int(data[i - 1])
        ) % MODULUS

    return result.astype(
        np.uint8
    )


def backward_diffusion(
    data,
    keystream
):
    """
    Backward modular diffusion.

    C[last] = (
        P[last]
        + K[last]
    ) mod 256

    C[i] = (
        P[i]
        + K[i]
        + 3 * C[i+1]
    ) mod 256
    """

    data = np.asarray(
        data,
        dtype=np.uint16
    )

    keystream = np.asarray(
        keystream,
        dtype=np.uint16
    )

    if data.shape != keystream.shape:
        raise ValueError(
            "Data and keystream must have "
            "the same shape."
        )

    if len(data) == 0:
        return np.array(
            [],
            dtype=np.uint8
        )

    result = np.empty(
        len(data),
        dtype=np.uint16
    )

    last = len(data) - 1

    # Last element
    result[last] = (
        int(data[last])
        + int(keystream[last])
    ) % MODULUS

    # Remaining elements
    for i in range(
        last - 1,
        -1,
        -1
    ):

        result[i] = (
            int(data[i])
            + int(keystream[i])
            + FEEDBACK_MULTIPLIER
            * int(result[i + 1])
        ) % MODULUS

    return result.astype(
        np.uint8
    )


def inverse_backward_diffusion(
    data,
    keystream
):
    """
    Reverse backward modular diffusion.

    P[last] = (
        C[last]
        - K[last]
    ) mod 256

    P[i] = (
        C[i]
        - K[i]
        - 3 * C[i+1]
    ) mod 256
    """

    data = np.asarray(
        data,
        dtype=np.uint16
    )

    keystream = np.asarray(
        keystream,
        dtype=np.uint16
    )

    if data.shape != keystream.shape:
        raise ValueError(
            "Data and keystream must have "
            "the same shape."
        )

    if len(data) == 0:
        return np.array(
            [],
            dtype=np.uint8
        )

    result = np.empty(
        len(data),
        dtype=np.uint16
    )

    last = len(data) - 1

    # Last element
    result[last] = (
        int(data[last])
        - int(keystream[last])
    ) % MODULUS

    # Remaining elements
    for i in range(
        last - 1,
        -1,
        -1
    ):

        result[i] = (
            int(data[i])
            - int(keystream[i])
            - FEEDBACK_MULTIPLIER
            * int(data[i + 1])
        ) % MODULUS

    return result.astype(
        np.uint8
    )