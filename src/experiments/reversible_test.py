from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import math


theta = math.pi / 3

qc = QuantumCircuit(2)

# Encryption transformation
qc.h(0)
qc.cx(0, 1)
qc.ry(theta, 1)

print("After encryption:")
print(qc)

# Inverse transformation
qc.ry(-theta, 1)
qc.cx(0, 1)
qc.h(0)

print("\nAfter decryption:")
print(qc)

simulator = AerSimulator()

qc.save_statevector()

result = simulator.run(qc).result()

statevector = result.get_statevector()

print("\nFinal state:")
print(statevector)