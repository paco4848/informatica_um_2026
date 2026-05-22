#Ejercicio 2
Celsius = float(input("Temperatura en ºC: "))
Conversion_C_a_F = Celsius * 9/5 + 32
print(f"{Celsius}ºC equivales a {Conversion_C_a_F:.2f}ºF")

F = float(input("Temperatura en ºF: "))
Conversion_F_a_C = (F-32) * 5/9 
print(f"{F}ºF equivales a {Conversion_F_a_C:.2f}ºC")