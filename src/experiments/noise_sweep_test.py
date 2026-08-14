from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

from src.noise.noise_models import (
    create_depolarizing_noise_model
)


def build_test_circuit():

    circuit = QuantumCircuit(
        4,
        4
    )

    circuit.h(0)
    circuit.h(1)

    circuit.cx(0, 2)
    circuit.cx(1, 3)

    circuit.ry(
        0.5,
        0
    )

    circuit.rz(
        1.0,
        1
    )

    circuit.cx(2, 3)

    circuit.measure(
        [0, 1, 2, 3],
        [0, 1, 2, 3]
    )

    return circuit


circuit = build_test_circuit()


NOISE_LEVELS = [
    0.0,
    0.001,
    0.005,
    0.01,
    0.02,
    0.05
]


SHOTS = 1000
SEED = 12345


print("=" * 70)
print("PHASE 7 - DEPOLARIZING NOISE SWEEP")
print("=" * 70)


for error_rate in NOISE_LEVELS:

    print(
        f"\nNoise level: "
        f"{error_rate:.3f}"
    )


    # -----------------------------------------
    # Ideal case
    # -----------------------------------------

    if error_rate == 0:

        simulator = AerSimulator(
            seed_simulator=SEED
        )


    # -----------------------------------------
    # Noisy case
    # -----------------------------------------

    else:

        noise_model = (
            create_depolarizing_noise_model(
                single_qubit_error=error_rate,
                two_qubit_error=error_rate
            )
        )

        simulator = AerSimulator(
            noise_model=noise_model,
            seed_simulator=SEED
        )


    result = (
        simulator
        .run(
            circuit,
            shots=SHOTS
        )
        .result()
    )


    counts = (
        result.get_counts()
    )


    print(
        "Counts:"
    )

    print(
        counts
    )


print("\n" + "=" * 70)
print("NOISE SWEEP COMPLETE")
print("=" * 70)