from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import math


theta = math.pi / 3

qc = QuantumCircuit(1)

qc.h(0)
qc.rz(theta, 0)

print(qc)

simulator = AerSimulator()

qc.save_statevector()

result = simulator.run(qc).result()

statevector = result.get_statevector()

print("\nStatevector:")
print(statevector)

print("\nProbabilities:")
print(statevector.probabilities_dict())