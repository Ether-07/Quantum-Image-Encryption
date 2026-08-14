from qiskit import QuantumCircuit


qc = QuantumCircuit(4)

qc.h(0)
qc.h(1)

qc.cx(0, 2)
qc.cx(1, 3)

qc.ry(0.7, 2)
qc.rz(1.2, 3)

qc.cx(2, 3)

print("Number of qubits:", qc.num_qubits)
print("Number of gates:", qc.size())
print("Circuit depth:", qc.depth())
print("Gate counts:", qc.count_ops())

print("\nCircuit:")
print(qc)