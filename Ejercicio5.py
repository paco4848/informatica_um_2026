print("punto 1:")
Punto_1x = int(input(" x1: "))
Punto_1y = int(input(" y1: ")) 
print("punto 2:")
Punto_2x = int(input(" x2: "))
Punto_2y = int(input(" y2: ")) 
Distancia = ((Punto_2x - Punto_1x) **2 + (Punto_2y - Punto_1y)**2)**0.5
print(f"Distancia entre ({Punto_1x}, {Punto_1y}) y ({Punto_2x}, {Punto_2y}) = {Distancia:.1f}")