def oracle_box(qc, hidden_code):

    # Get the length of the binary string
    length = len(hidden_code)

    # Create a quantum circuit with the given length
    for i in range(length):
        if hidden_code[i] == '1':
            qc.cx(i, length)

