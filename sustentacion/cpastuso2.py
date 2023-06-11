utiles = [{'id': 1, 'nombre': 'Lápiz'}, {'id': 2, 'nombre': 'Borrador'}]

def mostrar_lista():
    print("Lista de útiles escolares:")
    for util in utiles:
        print(f"{util['id']}. {util['nombre']}")

def modificar_util_por_id():
    mostrar_lista()
    id_util = int(input("Ingrese el ID del útil que desea modificar: "))
    for util in utiles:
        if util['id'] == id_util:
            nuevo_nombre = input("Ingrese el nuevo nombre del útil: ")
            util['nombre'] = nuevo_nombre
            print("¡El útil ha sido modificado correctamente!")
            return
    print("El ID del útil no se encontró en la lista.")

def buscar_util_por_nombre():
    nombre_util = input("Ingrese el nombre del útil que desea buscar: ")
    for util in utiles:
        if util['nombre'] == nombre_util:
            return util
    return None

def modificar_util():
    util = buscar_util_por_nombre()
    if util is not None:
        nuevo_nombre = input("Ingrese el nuevo nombre del útil: ")
        util['nombre'] = nuevo_nombre
        print("¡El útil ha sido modificado correctamente!")