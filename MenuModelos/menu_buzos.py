import time


def menu_buzos(CompraTotal, CompraProductos):
    modelo = 0
    cantidad = 0
    precio = 0.0
    nombreModelo = ""
    agregarOpcion = 0
    salida = False
    compra = 0

    print("..................................................................................................")
    print("::                                         CATEGORIA BUZOS                                      ::")
    print("::                                        MODELOS DISPONIBLES                                   ::")
    print("::..............................................................................................::")
    print("")

    print("1. Buzo Essential: $12740")
    print("2. Buzo Hoodie: $11950")
    print("3. Buzo Shadow: $12580")
    print("4. Buzo Flock: $13000")
    print("5. Buzo Saona: $13320")
    print("6. Buzo Lorain: $12800")
    print("7. Volver.")
    print(" ")
    modelo = int(input("Ingrese la opcion del modelo: "))

    if modelo == 7:
        salida = True
        # LimpiarPantalla()
        Productos()
    else:
        if modelo == 1:
            nombreModelo = "Buzo Essential"
            precio = 12740
        elif modelo == 2:
            nombreModelo = "Buzo Hoodie"
            precio = 11950
        elif modelo == 3:
            nombreModelo = "Buzo Shadow"
            precio = 12580
        elif modelo == 4:
            nombreModelo = "Buzo Flock"
            precio = 13000
        elif modelo == 5:
            nombreModelo = "Buzo Saona"
            precio = 13320
        elif modelo == 6:
            nombreModelo = "Buzo Lorain"
            precio = 12800

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