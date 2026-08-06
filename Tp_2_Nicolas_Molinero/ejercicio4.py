parrafo = input("Ingresa un texto: ")
palabras = parrafo.split()
cantidad_de_palabras = len(palabras)
cantidad_vocales = 0
vocales = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U", "á", "é", "í", "ó", "ú", "Á", "É", "Í", "Ó", "Ú"]
for c in parrafo:
    if c in "aeiouAEIOUáéíóúÁÉÍÓÚ":
        cantidad_vocales += 1
l = palabras[::-1]
juntar = " ".join(l)
palabra_larga = palabras[0]
for p in palabras:
    if len(p) > len(palabra_larga):
        palabra_larga = p
palabra_corta = palabras[0]
for p in palabras:
    if len(p) < len(palabra_corta) and p != " ":
        palabra_corta = p
sin_vocales = parrafo
for c in vocales:
    sin_vocales = sin_vocales.replace(c, "*")

print(f"Palabras: {cantidad_de_palabras}")
print(f"Vocales: {cantidad_vocales}")
print(f"Mas larga: {palabra_larga}")
print(f"Mas corta: {palabra_corta}")
print(f"Sin vocales: {sin_vocales}")
print(f"Orden inverso: {juntar}")