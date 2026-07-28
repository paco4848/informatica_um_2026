libros = []
biblioteca = 0
def mostrar_menu():
    while True:
       menu = print(f"=== BIBLIOTECA ===\n 1. Agregar libro \n 2. Listar todos los libros \n 4. Prestar libro \n 5. Devolver libro \6. Listar solo disponibles \n 7. Listar solo prestados \n 8. Estadísticas \n 9. Salir ")
    if menu == 1:
        print()
def agregar_libro(biblioteca, titulo, autor, año):
    while True:
        libro = intp