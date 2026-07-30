biblioteca = [
    {"titulo": "Cien anos de soledad", "autor": "Gabriel Garcia Marquez", "anio": "1967", "prestado": False},
    {"titulo": "El principito", "autor": "Antoine de Saint-Exupery", "anio": "1943", "prestado": False},
    {"titulo": "1984", "autor": "George Orwell", "anio": "1949", "prestado": True},
    {"titulo": "Don Quijote de la Mancha", "autor": "Miguel de Cervantes", "anio": "1605", "prestado": False},
    {"titulo": "Rayuela", "autor": "Julio Cortazar", "anio": "1963", "prestado": True}
]

# Variables globales obligatorias
libros_prestados_estadistica = 2  # Hay 2 prestados en la lista inicial (1984 y Rayuela)
titulo = ""
autor = ""
anio = ""



def mostrar_menu():
    while True:
        menu = input(
            "\n=== BIBLIOTECA ===\n"
            " 1. Agregar libro \n"
            " 2. Listar todos los libros \n"
            " 3. Buscar libro por título \n"
            " 4. Prestar libro \n"
            " 5. Devolver libro \n"
            " 6. Listar solo disponibles \n"
            " 7. Listar solo prestados \n"
            " 8. Estadísticas \n"
            " 9. Salir\n"
            "Selecciona una opción: "
        )

        if menu == "1":
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
                if p["prestado"] == False:
                    libros_disponibles.append(p["titulo"])
            print("Libros disponibles:", libros_disponibles)
        elif menu == "7":
            libros_prestados = []
            for p in biblioteca:
                if p["prestado"] == True:
                    libros_prestados.append(p["titulo"])
            print("Libros prestados:", libros_prestados)
        elif menu == "8":
            estadisticas(biblioteca)
        elif menu == "9":
            print("¡Saliendo del programa!")
            break


def agregar_libro(biblioteca, titulo, autor, anio):
    titulo = input("Coloca el titulo del libro: ")
    autor = input("Coloca el nombre del autor: ")
    anio = input("Coloca el año de creacion del libro: ")
    prestado = False
    
    # Se usa "anio" para ser consistente con la lista inicial
    biblioteca.append({"titulo": titulo, "autor": autor, "anio": anio, "prestado": prestado})
    print(f"Libro '{titulo}' agregado con éxito.")


def buscar_libro(biblioteca, titulo):
    titulo = input("Cual es el titulo del o los libros que buscas: ")
    nombre_libros = []
    for p in biblioteca:
        if titulo.lower() in p["titulo"].lower():
            # append solo recibe 1 argumento, así que guardamos una tupla con los datos
            nombre_libros.append((p["titulo"], p["autor"], p["anio"], p["prestado"]))
    print("Resultados:", nombre_libros)


def listar_libros(biblioteca):
    n = 0
    for p in biblioteca:
        n += 1
        estado = "Prestado" if p["prestado"] else "Disponible"
        print(f"{n}. {p['titulo']}, {p['autor']}, {p['anio']} [{estado}]")


def prestar(biblioteca, libro):
    global libros_prestados_estadistica
    libro = input("Que libro quieres que te prestemos: ").lower()
    encontrado = False
    
    for p in biblioteca:
        if p["titulo"].lower() == libro:
            encontrado = True
            if p["prestado"] == True:
                print("El libro ya esta prestado.")
            else:
                p["prestado"] = True
                libros_prestados_estadistica += 1
                print("Se te prestara el libro.")
            break
            
    if not encontrado:
        print("El libro que buscas no existe.")
        
    return libros_prestados_estadistica


def devolver(biblioteca, libro):
    libro = input("Que libro quieres devolver: ").lower()
    encontrado = False
    
    for p in biblioteca:
        if p["titulo"].lower() == libro:
            encontrado = True
            if p["prestado"] == False:
                print("El libro ya esta en la biblioteca.")
            else:
                p["prestado"] = False
                libros_prestados_estadistica -= 1
                print("Se devolvio el libro con exito.")
            break
    return libros_prestados_estadistica
    if not encontrado:
        print("El libro especificado no pertenece a la biblioteca.")
        


def estadisticas(biblioteca):
    print(f"La cantidad de libros prestados son: {libros_prestados_estadistica}")
    print(f"Los libros que hay disponibles son: {len(biblioteca) - libros_prestados_estadistica}")


# Inicio del programa
mostrar_menu()