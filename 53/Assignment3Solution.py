def fibonacci_recursive(n, sequence=None):
    if sequence is None:
        sequence = []
    if n <= 0:
        return sequence
    if len(sequence) < 2:
        sequence.append(0 if len(sequence) == 0 else 1)
    else:
        sequence.append(sequence[-1] + sequence[-2])
    return fibonacci_recursive(n - 1, sequence)

# Example usage
n = 10
print(fibonacci_recursive(n))
