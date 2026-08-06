def validar_pasword(pwd):
    ocho_caracteres = False
    mayusculas = False
    minusculas = False
    digitos = False
    especial = False
    if len(pwd) > 8:
        ocho_caracteres = True
    for caracter in pwd:
        if caracter.isupper():
            mayusculas = True
        if caracter.islower():
            minusculas = True
        if caracter.isdigit():
            digitos = True
        if caracter in "!@#$%&*?":
            especial = True
    errores = []
    if ocho_caracteres == False:
        errores.append("- Al menos 8 caracteres")
    if mayusculas == False:
        errores.append("- Al menos una letra mayúscula")
    if minusculas == False:
        errores.append("- Al menos una letra minuscula")
    if digitos == False:
        errores.append("- Al menos un digito")
    if especial == False:
        errores.append("- Al menos un carácter especial")
        return errores



pwd = input("ingrese una contraseña: ")
lista_errores = validar_pasword(pwd)
if len(lista_errores) > 0:
    print("Se encontraron los siguientes problemas:")
    for error in lista_errores:
        print(f"{error}")
