M = int(input("Quantas linhas vai ter essa matriz : "))
y = int(input("Quantas colunas vai ter essa matriz : "))

mat : [[int]] = [[0 for x in range(M)] for x in range(y)]

for i in range(0, M):
    for j in range(0, y):
        mat[i][j] = int(input(f"Elemento [{i},{j}]: "))

print()
print("MATRIZ DIGITADA : ")

for i in range (0,M):
    for j in range (0,y):
        print(f"{mat[i][j]} ", end="")
    print()