base = int(input("Digite a base do terreno : "))
altura = int(input("Digite a altura do terreno : "))

area = base * altura
perimetro = (base*2) + (altura*2)
diagonal = (base**2 + altura**2) ** (1/2)

print(f"Area = {area : .4f}")
print(f"Perimetro = {perimetro : .4f}")
print(f"Diagonal = {diagonal : .4f}")