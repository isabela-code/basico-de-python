x = int(input("Quantos numeros voce vai digitar : "))

soma = 0 

for i in range (0, x) :
    y = int(input("Digite um numero : "))
    soma = soma + y
    
print(f"Soma = {soma}")