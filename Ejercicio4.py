#Calcula la área y el perímetro de un circulo
pi = 3.14159
Radio = float(input("Radio del circulo: "))
Area = pi * Radio**2
Perimetro = 2 * pi * Radio
print(f"Para un círculo de radio {Radio} ")
print(f" Área:      {Area:.2f} unidades²")
print(f" Perímetro: {Perimetro:.2f} unidades")