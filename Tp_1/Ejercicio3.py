#Calcula la área y el perímetro de un rectangulo
base = float(input("Base del rectangulo: "))
altura = float(input("Altura del rectangulo: "))
area = base * altura
perimetro = 2 * (base + altura)
print("Resultados: ")
print(f" Área:      {area:.2f}m²")
print(f" Perímetro: {perimetro:.2f}m²")