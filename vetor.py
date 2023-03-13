x = int(input("Quantos numeros voce vai digitar : "))
vet = [0 for x in range (x)]

for i in range (0,x):
    vet[i] = float(input("Digite um numero : "))
    
print()
print("NUMERO DIGITADOS")

for i in range (0,x):
    print(f"{vet[i] : {x}}")