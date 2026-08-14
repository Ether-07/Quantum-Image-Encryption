from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import math


theta1 = math.pi / 3
theta2 = math.pi / 5

qc = QuantumCircuit(4)

# Create initial superposition
qc.h(0)
qc.h(1)

# Entangle qubits
qc.cx(0, 2)
qc.cx(1, 3)

# Key-dependent rotations
qc.ry(theta1, 2)
qc.rz(theta2, 3)

# Additional mixing
qc.cx(2, 3)
qc.cry(theta1, 3, 0)

print("Quantum mixing circuit:")
print(qc)

simulator = AerSimulator()

qc.save_statevector()

result = simulator.run(qc).result()

statevector = result.get_statevector()

print("\nStatevector:")
print(statevector)

print("\nProbabilities:")
print(statevector.probabilities_dict())

print("\nCircuit depth:")
print(qc.depth())

print("\nNumber of gates:")
print(qc.size())