from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import hashlib
import math


def key_to_angles(key):
    digest = hashlib.sha256(key.encode()).digest()

    angle1 = (digest[0] / 255) * 2 * math.pi
    angle2 = (digest[1] / 255) * 2 * math.pi

    return angle1, angle2


key = "MySecretKey123"

theta1, theta2 = key_to_angles(key)

print("Key:", key)
print("Theta 1:", theta1)
print("Theta 2:", theta2)

qc = QuantumCircuit(2)

qc.h(0)
qc.cx(0, 1)
qc.ry(theta1, 0)
qc.rz(theta2, 1)

print("\nCircuit:")
print(qc)

simulator = AerSimulator()

qc.save_statevector()

result = simulator.run(qc).result()

statevector = result.get_statevector()

print("\nStatevector:")
print(statevector)