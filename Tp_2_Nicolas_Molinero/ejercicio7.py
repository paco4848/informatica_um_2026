biblioteca =[{"titulo": "Cien anos de soledad", "autor": "Gabriel Garcia Marquez", "anio": "1967", "prestado": False},
{"titulo": "El principito", "autor": "Antoine de Saint-Exupery", "anio": "1943", "prestado": False},
{"titulo": "1984", "autor": "George Orwell", "anio": "1949", "prestado": True},
{"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "anio": "1605", "prestado": False},
{"titulo": "Rayuela", "autor": "Julio Cortazar", "anio": "1963", "prestado": True}
]
titulo = ""
autor = ""
anio = ""
def mostrar_menu():
    while True:
        menu = input(f"=== BIBLIOTECA ===\n 1. Agregar libro \n 2. Listar todos los libros \n 3. Buscar libro por título \n 4. Prestar libro \n 5. Devolver libro \n 6. Listar solo disponibles \n 7. Listar solo prestados \n 8. Estadísticas \n 9. Salir\n")
        if menu == "1" :
            agregar_libro(biblioteca, titulo, autor, anio)
        elif menu == "2":
            listar_libros(biblioteca)
        elif menu == "3":
            buscar_libro(biblioteca, titulo)
        elif menu == "4":
            prestar(biblioteca, titulo)
        elif menu == "5":
            devolver(biblioteca, titulo)
        elif menu == "6":
            libros_disponibles = []
            for p in biblioteca:
                if not p["prestado"] :
                    libros_disponibles.append(p["titulo"])
                    print(libros_disponibles)
        elif menu == "7":
            for p in biblioteca:
                if p["prestado"] == True:
                    print(f"{p['titulo']}")
        elif menu == "8":
            estadisticas(biblioteca)
        
        elif menu == "9":
            break
        else:
            print("opccion no valida")
    return
def agregar_libro(biblioteca, titulo, autor, anio):
    while True:
        titulo = input("coloca el nombre del libro o fin para salir:")
        if titulo.upper() == "FIN":
            break
        else:
            autor = input("Coloca el nombre del autor: ")
            anio = input("Coloca el año de creacion del libro: ")
            prestado = False
            biblioteca.append({"titulo": titulo, "autor": autor, "anio": anio, "prestado": prestado})
    return

def buscar_libro(biblioteca, titulo):
    nombre = input("Cual es el titulo del o los libros de buscas: ")
    nombre_libros = []
    for p in biblioteca:
        if nombre.lower() in p["titulo"].lower():
            nombre_libros.append((p["titulo"], p["autor"], p["anio"]))
    print(f"Los resultados son: {p["titulo"], p["autor"], p["anio"]}")
    return

def listar_libros(biblioteca):
    n = 0
    for p in biblioteca:
        n += 1
        print(f"{n}. {p["titulo"]}, {p["autor"]}, {p["anio"]}")

def prestar(biblioteca, libro):
    libro = input("Que libro quieres que te prestemos: ").lower()
    encontrado = False
    for p in biblioteca:
        if p["titulo"].lower() == libro and p["prestado"] == True:
            encontrado = True
            print("El libro ya esta prestado")
        elif p["titulo"].lower() == libro and p["prestado"] == False:
            encontrado = True
            print("Se te prestara el libro")
            p["prestado"] = True
            break
    if not encontrado:
        print("El libro que buscas no existe")
    return
    

def devolver(biblioteca, libro):
    libro = input("Que libro quieres devolver: ").lower()
    encontrado = False
    for p in biblioteca:
        if p["titulo"].lower() == libro and p["prestado"] == False:
            encontrado = True
            print("El libro ya esta en la biblioteca")
        elif p["titulo"].lower() == libro and p["prestado"] == True:
            encontrado = True
            print("Se delvovio el libro con exito")
            p["prestado"] = False
            break
    if not encontrado:
            print("El libro que buscas no existe")
    return

def estadisticas(biblioteca):
    libros_prestados_estadistica = 2
    for p in biblioteca:
        if p["prestado"] == True:
            libros_prestados_estadistica += 1
    print(f"La cantidad de libros prestados son: {libros_prestados_estadistica}")
    print(f"Los libros que hay son {len(biblioteca) - libros_prestados_estadistica}")
    return
mostrar_menu()