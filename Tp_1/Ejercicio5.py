#Calcula la distantancia desde un punto hacia otro punto
print("punto 1:")
punto_1x = int(input(" x1: "))
punto_1y = int(input(" y1: ")) 
print("punto 2:")
punto_2x = int(input(" x2: "))
punto_2y = int(input(" y2: ")) 
distancia = ((punto_2x - punto_1x) **2 + (punto_2y - punto_1y)**2)**0.5
print(f"Distancia entre ({punto_1x}, {punto_1y}) y ({punto_2x}, {punto_2y}) = {distancia:.1f}")