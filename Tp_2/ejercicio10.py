ccifrado = []
n = 3
def cifrado(texto, n):
    ccifrado = []
    for letra in texto:
        if ord(letra) >= ord("A") and ord(letra) <= ord("Z"):
            codigo = ord(letra) - ord("A")
            nuevo_codigo = (codigo + n) % 26
            ccifrado.append(chr(nuevo_codigo + ord("A")))
        elif letra >= "a" and letra <= "z":
            codigo = ord(letra) - ord("a")
            nuevo_codigo = (codigo + n) % 26
            ccifrado.append(chr(nuevo_codigo + ord("A")))
        else:
            ccifrado.append(letra)
    unir = "".join(ccifrado)
    print(unir)

def descifrado(texto, n):
        for letra in texto:
            if ord(letra) >= ord("A") and ord(letra) <= ord("Z"):
                codigo = ord(letra) - ord("A")
                nuevo_codigo = (codigo - n) % 26
                ccifrado.append(chr(nuevo_codigo + ord("A")))
            elif letra >= "a" and letra <= "z":
                codigo = ord(letra) - ord("a")
                nuevo_codigo = (codigo - n) % 26
                ccifrado.append(chr(nuevo_codigo + ord("A")))
            else:
                ccifrado.append(letra)
            unir = "".join(ccifrado)
        print(unir)
while True:
    print("Menu \n 1.cifrar \n 2.Desifrar \n 3.salir ")
    opcion = input("Elije una opcion: ")
    if opcion == "1":
            texto = input("Texto a cifrar: ")
            n = int(input("Desplazamiento (número): "))
            resultado = cifrado(texto, n)
            print(f"Texto cifrado: {resultado}")

    elif opcion == "2":
        texto = input("Texto a descifrar: ")
        n = int(input("Desplazamiento (número): "))
        resultado = descifrado(texto, n)
        print(f"Texto descifrado: {resultado}")

    elif opcion == "3":
        break
    else:
        print("Opción no válida. Intenta de nuevo.")



            
            



