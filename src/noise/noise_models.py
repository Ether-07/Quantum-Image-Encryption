from qiskit_aer.noise import (
    NoiseModel,
    depolarizing_error,
    ReadoutError
)


def create_depolarizing_noise_model(
    single_qubit_error=0.001,
    two_qubit_error=0.01
):
    """
    Create a depolarizing noise model.

    single_qubit_error:
        Error probability applied to
        single-qubit gates.

    two_qubit_error:
        Error probability applied to
        two-qubit gates.
    """

    if not (
        0 <= single_qubit_error <= 1
    ):
        raise ValueError(
            "single_qubit_error must be "
            "between 0 and 1."
        )

    if not (
        0 <= two_qubit_error <= 1
    ):
        raise ValueError(
            "two_qubit_error must be "
            "between 0 and 1."
        )


    noise_model = NoiseModel()


    # Single-qubit gate error
    single_error = (
        depolarizing_error(
            single_qubit_error,
            1
        )
    )


    # Two-qubit gate error
    two_error = (
        depolarizing_error(
            two_qubit_error,
            2
        )
    )


    noise_model.add_all_qubit_quantum_error(
        single_error,
        [
            "h",
            "ry",
            "rz"
        ]
    )


    noise_model.add_all_qubit_quantum_error(
        two_error,
        [
            "cx"
        ]
    )


    return noise_model


def create_readout_noise_model(
    probability_0_to_1=0.01,
    probability_1_to_0=0.01
):
    """
    Create a measurement/readout error model.

    probability_0_to_1:
        Probability that measured 0 becomes 1.

    probability_1_to_0:
        Probability that measured 1 becomes 0.
    """

    if not (
        0 <= probability_0_to_1 <= 1
    ):
        raise ValueError(
            "probability_0_to_1 must be "
            "between 0 and 1."
        )

    if not (
        0 <= probability_1_to_0 <= 1
    ):
        raise ValueError(
            "probability_1_to_0 must be "
            "between 0 and 1."
        )


    noise_model = NoiseModel()


    readout_error = ReadoutError(
        [
            [
                1 - probability_0_to_1,
                probability_0_to_1
            ],
            [
                probability_1_to_0,
                1 - probability_1_to_0
            ]
        ]
    )


    noise_model.add_all_qubit_readout_error(
        readout_error
    )


    return noise_model