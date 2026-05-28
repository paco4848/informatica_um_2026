Segundos = int(input("Cantidad de segundo: "))
hora = Segundos // 3600
resto = hora % 3600
minutos = Segundos // 60
total_de_segundos = resto % 60
print(f"{Segundos} segundos son equivalentes:")
print(f"  {hora} horas, {minutos} minutos y {total_de_segundos} segundos")