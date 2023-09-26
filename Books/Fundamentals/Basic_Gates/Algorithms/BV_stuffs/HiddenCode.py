import random

def generate_hidden_binary_string():
    # Generate a random length between 1 and 10
    length = random.randint(1, 10)
    
    # Generate a random binary string of the given length
    binary_string = ''.join(random.choices(['0', '1'], k=length))
    
    return binary_string

print(generate_hidden_binary_string())