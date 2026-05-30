#Es una aplicacion el cual dando tus años te dan tus dias, horas, minutos,segundos y latidos de corazon
year = int(input("¿Cuántos años tenes?"))
dias = year * 365
hora = dias * 24
minutos = hora * 60
segundos = minutos * 60
latidos = minutos * 70
print(f""" En {year} años aproximadamente viviste: 
       Dias:                {dias}
       Horas:               {hora}
       Minutos:             {minutos}
       segundos:            {segundos}
       Latidos del corazon: {latidos}""")
    