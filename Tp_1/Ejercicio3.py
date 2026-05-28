#Calcula la área y el perímetro de un rectangulo
Base = float(input("Base del rectangulo: "))
Altura = float(input("Altura del rectangulo: "))
Area = Base * Altura
Perimetro = 2 * (Base + Altura)
print("Resultados: ")
print(f" Área:      {Area:.2f}m²")
print(f" Perímetro: {Perimetro:.2f}m²")