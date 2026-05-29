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