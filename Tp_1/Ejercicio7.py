#Dando tu peso y altura calcula tu IMC y da que cuerpo tenes
Peso = float(input("Peso (Kg): "))
Altura = float(input("Altura (m): "))
imc = Peso / Altura**2
bajo_peso = imc < 18.5
peso_normal = imc > 18.5 and imc < 24.9
sobrepeso = imc > 25 and imc < 29.9
obesidad = imc > 30
print(f"IMC: {imc}")
print(f"Bajo peso: {bajo_peso}")
print(f"Peso normal: {peso_normal}")
print(f"Sobrepeso: {sobrepeso}")
print(f"Obesidad: {obesidad}")