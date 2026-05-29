#Convierte kilometros en millas y viseversa
kilometros = int(input("Ingresá kilómetros: "))
equivalencia_a_millas = kilometros/1.60934
print(f"{kilometros} km equivalen a {equivalencia_a_millas:.2f} millas")
millas= int(input("Ingresá millas: "))
equivalencia_a_kilometros = millas*1.60934
print(f"{millas} millas equivalen a {equivalencia_a_kilometros:.2f} km")
