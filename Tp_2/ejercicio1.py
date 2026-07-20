def  celsius_a_fahrenheit(c):
    return c * 9/5 + 32
def fahrenheit_a_celsius(f):
    return (f - 32) * 5/9
def celsius_a_kelvin(c):
    return c + 273.15
def kelvin_a_celsius(k):
    return k - 273.15
def fahrenheit_a_kelvin(f):
   c = (f - 32) * 5/9
   return c + 273.15
def kelvin_a_fahrenheit(k):
    c = k - 273.15
    return c * 9/5 + 32


temperatura = float(input("Temperatura: "))
origen = input("Unidad de origen (c/f/k): ")
destino = input("Unidad de destino (c/f/k): ")
if origen == "c" and destino == "f":
    print(f"{temperatura}º C equivalen a {celsius_a_fahrenheit(temperatura):.2f}º F")
elif origen == "c" and destino == "k":
    print(f"{temperatura}º C equivalen a {celsius_a_kelvin(temperatura):.2f}º K")
elif origen == "f" and destino == "c":
    print(f"{temperatura}º F equivalen a {fahrenheit_a_celsius(temperatura):.2f}º C")
elif origen == "f" and destino == "k":
    print(f"{temperatura}º F equivalen a {fahrenheit_a_kelvin(temperatura):.2f}º K")
elif origen == "k" and destino == "f":
    print(f"{temperatura}º K equivalen a {kelvin_a_fahrenheit(temperatura):.2f}º F")