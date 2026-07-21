""""
nota = int(input("dime una nota del 1/10: "))
asistencia = float(input("¿cual es tu porcentaje de asistencia? "))
if nota >= 8 and nota <= 10 and asistencia >=90:
    print("!Promocionado¡")
elif nota == 10:
    print("Sobresaliente")
elif nota > 10:
    print("esta mal")
elif nota< 0:
    print("esta mal")
elif  nota >= 8:
    print("Muy bien")
elif nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")
    """
n = int(input("¿Cuántas notas? "))
notas = []

for i in range(n):
    nota = float(input(f"Nota {i + 1}: "))
    notas.append(nota)

promedio = sum(notas) / len(notas)
aprobados = 0
for nota in notas:
    if nota >= 6: aprobados += 1

print(f"Notas: {notas} · Promedio: {promedio:.2f}")
print(f"Max: {max(notas)} · Min: {min(notas)} · Aprobados: {aprobados}")
