texto = "Hola mundo"
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

def desifrado(texto, n):
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
    opcion = input("elije una opcion \n 1.cifrar \n 2.Desifrar \n Elije: ")
    if opcion == "1":
        texto = input("Que texto para cifrar: ")
        n = ()



            
            



