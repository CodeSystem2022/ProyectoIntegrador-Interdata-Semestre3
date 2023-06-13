import time


def menu_trajes(CompraTotal, CompraProductos):
    modelo = 0
    cantidad = 0
    precio = 0.0
    nombreModelo = ""
    agregarOpcion = 0
    salida = False
    compra = 0

    print("..................................................................................................")
    print("::                                         CATEGORIA TRAJES                                     ::")
    print("::                                        MODELOS DISPONIBLES                                   ::")
    print("::..............................................................................................::")
    print("")

    print("1. Traje Pudong: $46740")
    print("2. Traje Quito: $45950")
    print("3. Traje Shangai: $49580")
    print("4. Traje Boston: $51800")
    print("5. Volver")
    print(" ")
    modelo = int(input("Ingrese la opcion del modelo: "))

    if modelo == 5:
        salida = True
        # LimpiarPantalla()
        Productos()
    else:
        if modelo == 1:
            nombreModelo = "Traje Pudong"
            precio = 46740
        elif modelo == 2:
            nombreModelo = "Traje Quito"
            precio = 45950
        elif modelo == 3:
            nombreModelo = "Traje Shangai"
            precio = 49580
        elif modelo == 4:
            nombreModelo = "Traje Boston"
            precio = 51800

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