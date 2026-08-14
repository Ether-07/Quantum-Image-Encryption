from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

qc = QuantumCircuit(2, 2)

qc.x(0)

qc.cx(0, 1)

qc.measure([0, 1], [0, 1])

print(qc)

simulator = AerSimulator()

result = simulator.run(qc, shots=1000).result()

print(result.get_counts())