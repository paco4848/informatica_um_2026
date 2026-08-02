alumnos = []
while True:
    nombre = input("pon el nombre del alumno o fin para salir: ")
    if nombre.lower() == "fin":
        break
    else:
        parcial1 = float(input("pon la nota del primer parcial: "))
        parcial2 = float(input("pon la nota del segundo parcial: "))
        if parcial1 < 7 or parcial2 < 7:
            recuperatorio = input("hizo recupertorio (s/n): ")
            if recuperatorio.lower() == "s":
                recuperatorio = float(input("por la nota de recuperatorio: "))
            else:
                recuperatorio = "None"
        alumnos.append([nombre, parcial1, parcial2, recuperatorio])
for n in alumnos: 
    print(f"{nombre:<15}, {parcial1:<5}, {parcial2:<5} {recuperatorio:<5}")