def print_pattern_list_comprehension(n):
    for i in range(1, n + 1):
        print(' '.join(['*'] * i))

# Example usage
n = 4
print_pattern_list_comprehension(n)
