#Calcula la área y el perímetro de un circulo
PI = 3.14159
radio = float(input("Radio del circulo: "))
area = PI * radio**2
perimetro = 2 * PI * radio
print(f"Para un círculo de radio {radio} ")
print(f" Área:      {area:.2f} unidades²")
print(f" Perímetro: {perimetro:.2f} unidades")