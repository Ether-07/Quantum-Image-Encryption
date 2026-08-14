from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


qc = QuantumCircuit(2)

qc.h(0)
qc.h(1)

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