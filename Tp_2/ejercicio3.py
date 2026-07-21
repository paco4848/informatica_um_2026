n = int(input("¿Cuántas notas vas a cargar? "))
notas = []

for i in range(n):
    nota = float(input(f"Nota {i + 1}: "))
    notas.append(nota)
aprobados = 0
for nota in notas:
    if nota >= 6:
        aprobados += 1
promedio = sum(notas) / len(notas)
mayor = notas[0]
for nota in notas:
    if nota > mayor:
        mayor = nota
minimo = notas[0]
for nota in notas:
    if nota < minimo:
        minimo = nota
print(f"{aprobados} y {promedio:.2f}")
print(f"mayor {mayor}")
