n = int(input("Enter the number of lines: "))
for i in range(1, n + 1):
    print(f"{' ' * (n - i) * 2}{' '.join(map(str, range(1, 2 * i)))}")
