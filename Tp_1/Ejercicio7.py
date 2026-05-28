Peso = float(input("Peso (Kg): "))
Altura = float(input("Altura (m): "))
Imc = Peso / Altura**2
bajo_peso = Imc < 18.5
peso_normal = Imc > 18.5 and Imc < 24.9
sobrepeso = Imc > 25 and Imc < 29.9
obesidad = Imc > 30
print(f"IMC: {Imc}")
print(f"Bajo peso: {bajo_peso}")
print(f"Peso normal: {peso_normal}")
print(f"Sobrepeso: {sobrepeso}")
print(f"Obesidad: {obesidad}")