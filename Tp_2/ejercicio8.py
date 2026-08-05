import random
palabra = ["Sol", "camino", "libro", "ventana", "estrella", "Musica", "Jardin", "playa", "Tiempo", "aventura"]
palabra_seleccionada = random.choice(palabra).lower()

ocultar = len(palabra_seleccionada) * ["_"]
for n in range(6):
    letras_intentadas = []
    print("".join(ocultar))
    letra = input("Di una letra: ").lower()
    letras_intentadas.append(letra)
    print(f"letras_intentadas {letras_intentadas}")
    for i in range(len(palabra_seleccionada)):
        if palabra_seleccionada[i] == letra:
            ocultar[i] = letra
    if ocultar == palabra_seleccionada or palabra_seleccionada == letra:
        print("Palabra acertada")
        break  
if not palabra_seleccionada == letra:
    print(f"se te acavaron los intentos, la palabra era {palabra_seleccionada}")
    
            
            