"""
n = int(input("dime un numero: "))
total = 0
for i in range(1,n+1):
    total += i
print(f"N: {n}, suma= {total}")
"""
"""
n = int(input("N: "))
total = 1
for i in range(1,n+1):
    total *= i
print(f"N: {n}, factorial={total}")
"""

numero = 69
intentos = 0
while True:
    n = int(input("Cual es el numero: "))
    if n == numero:
        intentos += 1
        print(f"Acertaste tu cantidad de intentos fueron: {intentos}")
        break
    
    elif n > numero:
        print("muy alto")
        intentos += 1
    elif n < numero:
        print("muy bajo")
        intentos += 1

