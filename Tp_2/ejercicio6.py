def tabla_multiplicar(n):
    for i in range(10):
        resultado = n * (i + 1)
        print(f"{n} x {i + 1} = {resultado}")
def  tabla_completa(n):
    for fila in range(1, n + 1):
        print()
        for columna in range(1, n + 1):
            resultado = fila * columna
            print(f"{resultado}", end=" ")
    print()
def triangulo(altura):
    for fila in range(1, altura + 1):
        print()
        for columna in range(1, fila + 1):
            print("*", end=" ")
    print()
def triangulo_invertido(altura):
    for fila in range(altura, 0, -1):
        print()
        for columna in range(1, fila + 1):
            print("*", end=" ")
    print()   
while True:
    opcion = int(input("Elije una opcion \n1. Tabla de multiplicar \n2. Tabla completa \n3. Triangulo \n4. Triangulo invertido \nOpcion: "))
    if opcion == 1:
        n = int(input("Numero: "))
        tabla_multiplicar(n)
        break
    elif opcion == 2:
        n = int(input("Numero: "))
        tabla_completa(n)
        break
    elif opcion == 3:
        altura = int(input("Altura: "))
        triangulo(altura)
        break
    elif opcion == 4:
        altura = int(input("Altura: "))
        triangulo_invertido(altura)
        break
    else:
        print("opcion no valida, intenta de nuevo")
        

