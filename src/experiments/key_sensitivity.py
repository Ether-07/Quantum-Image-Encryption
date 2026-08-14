from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import hashlib
import math


def key_to_angles(key):
    digest = hashlib.sha256(key.encode()).digest()

    theta1 = (digest[0] / 255) * 2 * math.pi
    theta2 = (digest[1] / 255) * 2 * math.pi

    return theta1, theta2


def create_circuit(key):
    theta1, theta2 = key_to_angles(key)

    qc = QuantumCircuit(2)

    qc.h(0)
    qc.cx(0, 1)
    qc.ry(theta1, 0)
    qc.rz(theta2, 1)

    return qc


key1 = "QuantumKey123"
key2 = "QuantumKey124"

qc1 = create_circuit(key1)
qc2 = create_circuit(key2)

simulator = AerSimulator()

qc1.save_statevector()
qc2.save_statevector()

result1 = simulator.run(qc1).result()
result2 = simulator.run(qc2).result()

state1 = result1.get_statevector()
state2 = result2.get_statevector()

print("Key 1:", key1)
print("State 1:")
print(state1)

print("\nKey 2:", key2)
print("State 2:")
print(state2)