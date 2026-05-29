segundos = int(input("Cantidad de segundo: "))
hora = segundos // 3600
resto = hora % 3600
minutos = segundos // 60
total_de_segundos = resto % 60
print(f"{segundos} segundos son equivalentes:")
print(f"  {hora} horas, {minutos} minutos y {total_de_segundos} segundos")