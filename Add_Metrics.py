def add_matrices():
    m = int(input("Enter the number of rows: "))
    n = int(input("Enter the number of columns: "))

    matrix1 = []
    matrix2 = []
    result = []

    print("Enter elements of matrix1:")
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(input(f"Enter element ({i+1},{j+1}): ")))
        matrix1.append(row)

    print("Enter elements of matrix2:")
    for i in range(m):
        row = []
        for j in range(n):
            row.append(int(input(f"Enter element ({i+1},{j+1}): ")))
        matrix2.append(row)

    result = [[matrix1[i][j] + matrix2[i][j] for j in range(n)] for i in range(m)]

    print("Result:")
    for row in result:
        print(row)

add_matrices()