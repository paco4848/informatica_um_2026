alumnos = []
while True:
    nombre = input("pon el nombre del alumno o fin para salir: ")
    if nombre.lower() == "fin":
        break
    else:
        parcial1 = float(input("pon la nota del primer parcial: "))
        parcial2 = float(input("pon la nota del segundo parcial: "))
        recuperatorio = "None"
        if parcial1 >= 7 and parcial2 >= 7:
            promedio = (parcial1 + parcial2) / 2
        if parcial1 < 7 or parcial2 < 7:
            recuperatorio = input("hizo recupertorio (s/n): ")
            if recuperatorio.lower() == "s":
                recuperatorio = float(input("por la nota de recuperatorio: "))
                promedio = (max(parcial1, parcial2) + recuperatorio) / 2
            else:
                promedio = (parcial1 + parcial2) / 2
        if promedio >= 8:
            estado = "promocion"
        elif promedio >= 6:
            estado = "regular"
        else:
            estado = "libre" 
        alumnos.append([nombre, parcial1, parcial2, recuperatorio, promedio, estado])
for n in alumnos: 
    print(f"[{n[0]:<15}, {n[1]:<5}, {n[2]:<5} {n[3]:<5} {n[4]:<5} {n[5]:<9}]")