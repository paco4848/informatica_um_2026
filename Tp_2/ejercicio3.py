notas = []
while True:
     cantidad_notas = int(input("¿Cuántas notas vas a cargar? "))
     if cantidad_notas < 0:
         print("El número de notas no puede ser negativo.")
     else:
         break
for i in range(cantidad_notas):
    while True:
    
        nota = float(input(f"Nota {i + 1}: "))
        if 0 <= nota <= 10:
            notas.append(nota)
            break
        else:
            print("La nota ingresada no es válida. Debe estar entre 0 y 10.")
aprobados = 0
for nota in notas:
    if nota >= 6:
        aprobados += 1
    promedio = sum(notas) / len(notas)
porcentaje_aprobados = (aprobados / len(notas)) * 100
mayor = notas[0]
for nota in notas:
    if nota > mayor:
        mayor = nota
minimo = notas[0]
for nota in notas:
    if nota < minimo:
        minimo = nota
reprobados_graves = 0
reprobados = 0
regulares = 0
exelentes = 0
for nota in notas:
    if nota <= 3:
            reprobados_graves += 1
    elif 4 <= nota <= 5:
            reprobados += 1
    elif 6 <= nota <= 7:
            regulares += 1
    elif nota >= 8:
            exelentes += 1
print(f"===ANALISIS===")
print(f"Notas: {notas}")
print(f"Promedio: {promedio}")
print(f"Mayor nota: {mayor}")
print(f"Menor nota: {minimo}")
print(f"Aprobados: {aprobados}({porcentaje_aprobados:.0f}%)")
print(f"Distribución: {reprobados_graves} reprobados graves, {reprobados} reprobados, {regulares} regulares, {exelentes} exelentes")
