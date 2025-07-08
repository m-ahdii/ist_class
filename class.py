n = int(input("Enter a number to generate multiplication table: "))
layout = input("Choose layout (vertical or horizontal): ").strip().lower()

table = []

if layout == "horizontal":
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(i * j)
        table.append(row)

    print("\nMultiplication Table")
    print("    ", end="")
    for i in range(1, n + 1):
        print(f"{i:4}", end="")
    print("\n" + "-" * (5 * n))

    for i in range(n):
        print(f"{i+1:3}|", end="")
        for j in range(n):
            print(f"{table[i][j]:4}", end="")
        print()

elif layout == "vertical":
    for i in range(1, n + 1):
        row = []
        for j in range(1, n + 1):
            row.append(j * i)
        table.append(row)

    print("\nMultiplication Table")
    print("    ", end="")
    for i in range(1, n + 1):
        print(f"{i:4}", end="")
    print("\n" + "-" * (5 * n))

    for i in range(n):
        print(f"{i+1:3}|", end="")
        for j in range(n):
            print(f"{table[i][j]:4}", end="")
        print()

else:
    print("Invalid layout. Please type 'horizontal' or 'vertical'.")