import hashlib
import math

from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def key_to_angles(key):
    """
    Convert a key into deterministic quantum rotation angles.
    """

    digest = hashlib.sha256(
        key.encode("utf-8")
    ).digest()

    theta1 = (
        digest[0] / 255.0
    ) * 2 * math.pi

    theta2 = (
        digest[1] / 255.0
    ) * 2 * math.pi

    theta3 = (
        digest[2] / 255.0
    ) * 2 * math.pi

    return theta1, theta2, theta3


def build_quantum_circuit(
    theta1,
    theta2,
    theta3
):
    """
    Build the 4-qubit quantum mixing circuit.
    """

    qc = QuantumCircuit(4, 4)

    # Superposition
    qc.h(0)
    qc.h(1)

    # Entanglement
    qc.cx(0, 2)
    qc.cx(1, 3)

    # Key-dependent rotations
    qc.ry(theta1, 0)
    qc.rz(theta2, 1)
    qc.ry(theta3, 2)

    # Additional mixing
    qc.cx(2, 3)

    # Measurement
    qc.measure(
        [0, 1, 2, 3],
        [0, 1, 2, 3]
    )

    return qc


def generate_quantum_bits(
    key,
    number_of_bits,
    seed=12345
):
    """
    Generate deterministic quantum-derived bits.

    Circuits are executed in batches.

    This is a research prototype and is NOT
    a production cryptographic RNG.
    """

    if number_of_bits <= 0:
        return []

    theta1, theta2, theta3 = key_to_angles(
        key
    )

    bits = []

    # One circuit produces four measured bits.
    number_of_circuits = math.ceil(
        number_of_bits / 4
    )

    circuits = []

    for _ in range(number_of_circuits):

        circuit = build_quantum_circuit(
            theta1,
            theta2,
            theta3
        )

        circuits.append(circuit)

    simulator = AerSimulator(
        seed_simulator=seed
    )

    result = simulator.run(
        circuits,
        shots=1
    ).result()

    for index in range(
        number_of_circuits
    ):

        counts = result.get_counts(index)

        measured = next(
            iter(counts)
        )

        bits.extend(
            int(bit)
            for bit in measured
        )

    return bits[:number_of_bits]


def bits_to_bytes(bits):
    """
    Convert a list of bits into byte values.
    """

    if len(bits) % 8 != 0:
        raise ValueError(
            "Number of bits must be divisible by 8."
        )

    byte_values = []

    for i in range(
        0,
        len(bits),
        8
    ):

        byte_value = 0

        for bit in bits[i:i + 8]:

            byte_value = (
                byte_value << 1
            ) | bit

        byte_values.append(
            byte_value
        )

    return byte_values