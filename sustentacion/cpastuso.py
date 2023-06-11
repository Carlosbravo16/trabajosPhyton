ropa = []
op = 1


def agregar():
    agregar = input("ingrese el nombre de la prenda que desea agregar:")
    ropa.append(agregar)
    print(ropa)


def lista():
    for l in ropa:
        print(l)
    if len(ropa) == 0:
            print("la lista se encuentra vacia")
    else:
            cantidad = len(ropa)
            print(f"hay{cantidad} de prendas en la lista")


while op == 1:
    print("1 agregar prendas de ropa")
    print("2 lista de articulos")
    print("3 para salir")

    opcion = int(input("selecione una opcion \n"))
    if opcion == 1:
        agregar()
    elif opcion == 2:
        lista()
    elif opcion == 3:
        print("gracias vuelva pronto")

    op = int(input("1 para modificar la lista.\n2 para salir"))
