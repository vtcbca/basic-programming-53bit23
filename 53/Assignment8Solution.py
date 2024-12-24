n = int(input("Enter the number of lines: "))
for i in range(1, n + 1):
    print(f"{' ' * (n - i) * 2}{' '.join(chr(64 + j) for j in range(1, i + 1))} {' '.join(chr(64 + j) for j in range(i - 1, 0, -1))}")
