# Sistema de biblioteca
biblioteca = [
    {
        "codigo": "CL001",
        "titulo":"Don Quijote de la Mancha",
        "autor": "Cervantes",
        "genero": "Novela",
        "casa_editorial": "Letras Ibéricas",
        "tramo": "A-1",
        "estado": "en sala"
    },
    {
        "codigo": "CL002",
        "titulo":"Cien años de soledad",
        "autor": "García Márquez",
        "genero": "Realismo Mágico",
        "casa_editorial": "Editorial Macondo",
        "tramo": "A-2",
        "estado": "en sala"
    },
    {
        "codigo": "CL003",
         "titulo":"Orgullo y prejuicio",
        "autor": "Austen",
        "genero": "Romance",
        "casa_editorial": "Casa Pemberley",
        "tramo": "A-3",
        "estado": "en sala"
    },
    {
        "codigo": "CL004",
        "titulo":"Moby Dick",
        "autor": "Melville",
        "genero": "Aventura",
        "casa_editorial": "Ballena Blanca",
        "tramo": "A-4",
        "estado": "en sala"
    },
    {
        "codigo": "CL005",
         "titulo":"Guerra y paz",
        "autor": "Tolstói",
        "genero": "Histórico",
        "casa_editorial": "Editorial Rusa",
        "tramo": "A-5",
        "estado": "en sala"
    },

]


def ver_catalogo():
    print("\n--- Catálogo de libros ---")
    for libro in biblioteca:
        print(
            f"Código: {libro['codigo']}, titulo: {libro['titulo']}, Autor: {libro['autor']}, Género: {libro['genero']}, "
            f"Editorial: {libro['casa_editorial']}, Tramo: {libro['tramo']}, Estado: {libro['estado']}"
        )


def auto_servicio():
    ver_catalogo()
    codigo = input("\nIngresa el código del libro que deseas prestar: ")
    for libro in biblioteca:
        if libro["codigo"] == codigo:
            if libro["estado"] == "en sala":
                libro["estado"] = "prestado"
                print("Libro prestado exitosamente.")
            else:
                print("El libro ya está prestado.")
            return
    print("Código no encontrado.")


def agregar_libro():
    print("\n--- Agregar nuevo libro ---")
    nuevo_libro = {
        "codigo": input("Código del libro: "),
        "autor": input("Autor (nombre y apellido): "),
        "genero": input("Género: "),
        "casa_editorial": input("Casa editorial: "),
        "tramo": input("Tramo asignado: "),
        "estado": input("Estado (en sala/prestado): ")
    }
    biblioteca.append(nuevo_libro)
    print("Libro agregado exitosamente.")


def modificar_libro():
    ver_catalogo()
    codigo = input("\nIngresa el código del libro que deseas modificar: ")
    for libro in biblioteca:
        if libro["codigo"] == codigo:
            nuevo_codigo = input("Nuevo código del libro: ")
            libro["codigo"] = nuevo_codigo
            print("Código modificado exitosamente.")
            return
    print("Código no encontrado.")


def eliminar_libro():
    ver_catalogo()
    codigo = input("\nIngresa el código del libro que deseas eliminar: ")
    for libro in biblioteca:
        if libro["codigo"] == codigo:
            biblioteca.remove(libro)
            print("Libro eliminado exitosamente.")
            return
    print("Código no encontrado.")


def menu():
    while True:
        print("\n--- Menú de la biblioteca ---")
        print("1. Ver catálogo de libros")
        print("2. Auto servicio")
        print("3. Agregar libro")
        print("4. Modificar libro")
        print("5. Eliminar libro")
        print("6. Salir")

        opcion = input("Elige una opción: ")
        if opcion == "1":
            ver_catalogo()
        elif opcion == "2":
            auto_servicio()
        elif opcion == "3":
            agregar_libro()
        elif opcion == "4":
            modificar_libro()
        elif opcion == "5":
            eliminar_libro()
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")


# Ejecutar el menú
menu()

