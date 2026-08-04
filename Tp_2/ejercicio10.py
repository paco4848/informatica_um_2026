texto = "Hola mundo"
cifrado = []
def cifrado(texto, n):
    for letra in texto:
        if letra <= "A" and letra >= "Z":
            (letra + n) % 26

