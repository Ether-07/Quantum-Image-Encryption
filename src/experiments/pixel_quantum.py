from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator


def pixel_to_binary(value):
    return format(value, "08b")


pixel = 173

binary = pixel_to_binary(pixel)

print("Pixel:", pixel)
print("Binary:", binary)

qc = QuantumCircuit(8, 8)

# Qiskit displays qubit 7 on the left and qubit 0 on the right
for qubit, bit in enumerate(reversed(binary)):
    if bit == "1":
        qc.x(qubit)

qc.measure(range(8), range(8))

print("\nQuantum circuit:")
print(qc)

simulator = AerSimulator()

result = simulator.run(qc, shots=1000).result()

print("\nMeasurement:")
print(result.get_counts())