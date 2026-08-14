from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import math


theta = math.pi / 2

qc = QuantumCircuit(2)

qc.x(0)

qc.cry(theta, 0, 1)

print("Circuit:")
print(qc)

simulator = AerSimulator()

qc.save_statevector()

result = simulator.run(qc).result()

statevector = result.get_statevector()

print("\nStatevector:")
print(statevector)

print("\nProbabilities:")
print(statevector.probabilities_dict())