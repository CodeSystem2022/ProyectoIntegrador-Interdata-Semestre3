import time


def menu_joggings(CompraTotal, CompraProductos):
    modelo = 0
    cantidad = 0
    precio = 0.0
    nombreModelo = ""
    agregarOpcion = 0
    salida = False
    compra = 0

    print("..................................................................................................")
    print("::                                         CATEGORIA JOGGINGS                                   ::")
    print("::                                        MODELOS DISPONIBLES                                   ::")
    print("::..............................................................................................::")
    print("")

    print("1. Jogging Tanger: $12750")
    print("2. Jogging Munich: $12950")
    print("3. Jogging Sidney: $11580")
    print("4. Jogging Praga: $13000")
    print("5. Jogging Din: $13300")
    print("6. Jogging Tamesis: $12400")
    print("7. Volver.")
    print(" ")
    modelo = int(input("Ingrese la opcion del modelo: "))

    if modelo == 7:
        salida = True
        # LimpiarPantalla()
        Productos()
    else:
        if modelo == 1:
            nombreModelo = "Jogging Tanger"
            precio = 12750
        elif modelo == 2:
            nombreModelo = "Jogging Munich"
            precio = 12950
        elif modelo == 3:
            nombreModelo = "Jogging Sidney"
            precio = 11580
        elif modelo == 4:
            nombreModelo = "Jogging Praga"
            precio = 13000
        elif modelo == 5:
            nombreModelo = "Jogging Din"
            precio = 13300
        elif modelo == 6:
            nombreModelo = "Jogging Tamesis"
            precio = 12400

        if not salida:
            print("¿Aniadir al carrito? 1.Si -- 2.No: ")
            agregarOpcion = int(input())

        if agregarOpcion == 1:
            print("Cantidad: ", end="")
            cantidad = int(input())
            CompraProductos += nombreModelo
            # LimpiarPantalla()

            print(
                ".........................................................................................................")
            print("                                   :: AÑADIDO AL CARRITO ::                           ")
            print(
                ".........................................................................................................")
            print("Producto añadido al carrito: ", nombreModelo)
            print("Cantidad: ", cantidad)
            print("Precio por curva $: ", precio)
            Compra = precio * cantidad
            CompraTotal += (precio * cantidad)
            print("Precio total de lo añadido $: ", Compra)
            time.sleep(5)
            # LimpiarPantalla()
        elif agregarOpcion == 2:
            print("Volviendo a la sección productos")
            time.sleep(0.5)
            print("")
            print("Aguarde unos segundos ....")
            time.sleep(2)
            # LimpiarPantalla()