#cualcula todo lo que deberia ir en el resumen de una cuenta 
Monto = float(input("Monto de la cuenta: "))
Porcentaje = int(input("Porcentaje de propina (%): "))
Personas = int(input("Cantidad de personas: "))
Propina = Monto * (Porcentaje/100)
Total = Monto + Propina
Total_persona = Total / Personas
print("Resumen:")
print(f" Cuenta:                    ${Monto:.2f}")
print(f" Propina ({Porcentaje}):            ${Propina:.2f}")
print(f" Total:                     ${Total:.2f}")
print(f" Por persona:               {Total_persona:.2f}")