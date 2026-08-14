from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)

qc.h(0)
qc.cx(0, 1)

qc.measure([0, 1], [0, 1])

simulator = AerSimulator()

result = simulator.run(qc, shots=1000).result()

counts = result.get_counts()

print(counts)