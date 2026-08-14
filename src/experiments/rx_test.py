from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import math


theta = math.pi / 2

qc = QuantumCircuit(1)

qc.rx(theta, 0)

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