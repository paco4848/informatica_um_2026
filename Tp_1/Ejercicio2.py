#Convierte grados celsius a Fahrenheit y viseversa
celsius = float(input("Temperatura en ºC: "))
conversion_C_a_F = celsius * 9/5 + 32
print(f"{celsius}ºC equivales a {conversion_C_a_F:.2f}ºF")

farenheit = float(input("Temperatura en ºF: "))
conversion_f_a_c = (farenheit-32) * 5/9 
print(f"{farenheit}ºF equivales a {conversion_f_a_c:.2f}ºC")