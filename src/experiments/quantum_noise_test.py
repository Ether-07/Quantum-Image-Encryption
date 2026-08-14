from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

from src.noise.noise_models import (
    create_depolarizing_noise_model,
    create_readout_noise_model
)


def build_test_circuit():

    circuit = QuantumCircuit(
        4,
        4
    )


    # Superposition
    circuit.h(0)
    circuit.h(1)


    # Entanglement
    circuit.cx(0, 2)
    circuit.cx(1, 3)


    # Key-dependent style rotations
    circuit.ry(
        0.5,
        0
    )

    circuit.rz(
        1.0,
        1
    )


    # Additional mixing
    circuit.cx(2, 3)


    # Measurement
    circuit.measure(
        [0, 1, 2, 3],
        [0, 1, 2, 3]
    )


    return circuit


circuit = build_test_circuit()


SHOTS = 1000
SEED = 12345


print("=" * 70)
print("PHASE 7 - IDEAL VS NOISY QUANTUM SIMULATION")
print("=" * 70)


# ==================================================
# IDEAL
# ==================================================

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


print("\nIDEAL SIMULATION")
print("-" * 70)

print(
    ideal_counts
)


# ==================================================
# DEPOLARIZING NOISE
# ==================================================

depolarizing_model = (
    create_depolarizing_noise_model(
        single_qubit_error=0.001,
        two_qubit_error=0.01
    )
)


depolarizing_simulator = AerSimulator(
    noise_model=depolarizing_model,
    seed_simulator=SEED
)


depolarizing_result = (
    depolarizing_simulator
    .run(
        circuit,
        shots=SHOTS
    )
    .result()
)


depolarizing_counts = (
    depolarizing_result.get_counts()
)


print("\nDEPOLARIZING NOISE")
print("-" * 70)

print(
    depolarizing_counts
)


# ==================================================
# READOUT NOISE
# ==================================================

readout_model = (
    create_readout_noise_model(
        probability_0_to_1=0.01,
        probability_1_to_0=0.01
    )
)


readout_simulator = AerSimulator(
    noise_model=readout_model,
    seed_simulator=SEED
)


readout_result = (
    readout_simulator
    .run(
        circuit,
        shots=SHOTS
    )
    .result()
)


readout_counts = (
    readout_result.get_counts()
)


print("\nREADOUT NOISE")
print("-" * 70)

print(
    readout_counts
)


print("\n" + "=" * 70)
print("NOISE TEST COMPLETE")
print("=" * 70)