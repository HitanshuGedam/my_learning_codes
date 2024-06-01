import qiskit
import math
from qiskit import QuantumCircuit, Aer, execute
from qiskit.quantum_info import Statevector
from qiskit.visualization import plot_histogram

maximum = int(input("Enter maximum number: "))
maximum_bin = bin(maximum)[2:]
length = len(str(maximum_bin))
print(maximum, maximum_bin, length)
list_nums = [i for i in range(maximum + 1)]
print(list_nums)

list_binaries = [ bin(num)[2:].zfill(length) for num in range(int(maximum + 1))]
print(list_binaries)

wires = math.ceil(math.log(maximum, 2))
print(wires)

qc = QuantumCircuit(wires)
qc.h([i for i in range(wires)])
qc.measure_all()
qc.draw()

simulator = Aer.get_backend('qasm_simulator')
job = execute(qc, simulator, shots=maximum*1024)
result = job.result()
counts = result.get_counts(qc)
print(counts)

plot_histogram(counts)

random_number = int(list(counts.keys())[list(counts.values()).index(max(counts.values()))], 2)
random_number = random_number % maximum
print(random_number)
