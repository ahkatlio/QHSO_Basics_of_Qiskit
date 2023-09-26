from HiddenCode import generate_hidden_binary_string
from qiskit import QuantumCircuit

def oracle_box():
    # Get a random binary string
    hidden_code = generate_hidden_binary_string()

    # Get the length of the binary string
    length = len(hidden_code)

    # Create a quantum circuit with the given length
    qc = QuantumCircuit(length+1, length+1)
    for i in range(length):
        if hidden_code[i] == '1':
            qc.cx(i, length)
    return qc

