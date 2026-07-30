import random
palabra = ["Sol", "camino", "libro", "ventana", "estrella", "Musica", "Jardin", "playa", "Tiempo", "aventura"]
palabra_seleccionada = random.choice(palabra).lower()

print(palabra_seleccionada)
ocultar = len(palabra_seleccionada) * ["_"]
while True:
    print("".join(ocultar))
    letra = input("Di una letra: ").lower()
    for i in range(len(palabra_seleccionada)):
        if palabra_seleccionada[i] == letra:
            ocultar[i] = letra
    if ocultar ==palabra_seleccionada or palabra_seleccionada == letra:
        print("Palabra acertada")
        break
            
            
            