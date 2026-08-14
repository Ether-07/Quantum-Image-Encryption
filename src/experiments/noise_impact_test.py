from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

from src.noise.noise_models import (
    create_depolarizing_noise_model
)

from src.analysis.quantum_metrics import (
    total_variation_distance
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


SHOTS = 1000
SEED = 12345


# --------------------------------------------------
# Ideal reference
# --------------------------------------------------

ideal_simulator = AerSimulator(
    seed_simulator=SEED
)


ideal_result = (
    ideal_simulator
    .run(
        circuit,
        shots=SHOTS
    )
    .result()
)


ideal_counts = (
    ideal_result.get_counts()
)


# --------------------------------------------------
# Noise levels
# --------------------------------------------------

noise_levels = [
    0.001,
    0.005,
    0.01,
    0.02,
    0.05
]


print("=" * 70)
print("PHASE 7 - QUANTUM NOISE IMPACT")
print("=" * 70)


for error_rate in noise_levels:

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


    noisy_counts = (
        result.get_counts()
    )


    distance = (
        total_variation_distance(
            ideal_counts,
            noisy_counts
        )
    )


    print(
        f"\nNoise level: "
        f"{error_rate:.3f}"
    )

    print(
        f"Total variation distance: "
        f"{distance:.6f}"
    )


print("\n" + "=" * 70)
print("NOISE IMPACT TEST COMPLETE")
print("=" * 70)