while True:
    pregunta = input("hola quieres lanzar el dado? si o no?")
    if pregunta == "si":
        resultado = random.randint(1, 6)
        print("el resultado del dado es: ", resultado)
     elif pregunta == "no":
        print("bueno, hhasta luego")
        break
    else: print("pon que si para poder jugar")