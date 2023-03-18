largura = int(input("Digite a largura do terreno : "))
comprimento = int(input("Digite o comprimento do terreno : "))
metro = int(input("Digite o metro quadrado do terreno : "))

area = largura * comprimento 
valor = area * metro

print(f"Area do terreno = {area : .2f}")
print(f"Valor do terreno = {valor : .2f}")
