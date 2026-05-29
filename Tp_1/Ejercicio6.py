#cualcula todo lo que deberia ir en el resumen de una cuenta 
monto = float(input("Monto de la cuenta: "))
porcentaje = int(input("Porcentaje de propina (%): "))
personas = int(input("Cantidad de personas: "))
propina = monto * (porcentaje/100)
total = monto + propina
total_persona = total / personas
print("Resumen:")
print(f" Cuenta:                    ${monto:.2f}")
print(f" Propina ({porcentaje}):            ${propina:.2f}")
print(f" Total:                     ${total:.2f}")
print(f" Por persona:               {total_persona:.2f}")