""""
notas = [8, 6, 9, 4, 10, 7, 5, 8, 3, 9]
total = 0
aprobados = 0
desaprobado = 0
for nota in notas:
    total += nota
    if nota >= 6 :
        aprobados += 1
    else:
        desaprobado +=1
print(f"Total: {total} · Aprobados: {aprobados} · Desaprobados: {desaprobado}")
"""

N = int(input("notas a ingresar: "))
notas = []


for nota in range(N):
    nota = float(input("nota: "))
    notas.append(nota)
while True:
        promedio = sum(notas) / len(notas)
        aprobados = 0
        for nota in notas:
            if 6 >= nota:
             aprobados += 1
        print(f"Max: {max(notas)} · Min: {min(notas)} · Aprobados: {aprobados}")
        print(f"Notas: {notas} · Promedio: {promedio:.2f}")
        s = input("quieres colocar otro elemento (s/n): ") == "s"
        if s:
            nota = float(input("nota: "))
            notas.append(nota)
        else:
            print("Gracias por usar el programa")
            break