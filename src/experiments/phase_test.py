from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(1, 1)

qc.h(0)
qc.z(0)
qc.h(0)

qc.measure(0, 0)

print(qc)

simulator = AerSimulator()

result = simulator.run(qc, shots=1000).result()

print(result.get_counts())