from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


qc = QuantumCircuit(1)

qc.h(0)

print("Quantum circuit:")
print(qc)

simulator = AerSimulator()

qc.save_statevector()

result = simulator.run(qc).result()

statevector = result.get_statevector()

print("\nStatevector:")
print(statevector)