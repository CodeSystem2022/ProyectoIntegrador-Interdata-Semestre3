import time


def menu_camperas(CompraTotal, CompraProductos):
    modelo = 0
    cantidad = 0
    precio = 0.0
    nombreModelo = ""
    agregarOpcion = 0
    salida = False
    compra = 0

    print("..................................................................................................")
    print("::                                         CATEGORIA CAMPERAS                                   ::")
    print("::                                        MODELOS DISPONIBLES                                   ::")
    print("::..............................................................................................::")
    print("")

    print("1. Campera Moscu: $14000")
    print("2. Campera Morava: $15100")
    print("3. Campera Cesana: $16780")
    print("4. Campera Nuremberg: $15900")
    print("5. Campera Banff: $15320")
    print("6. Campera Rocker: $16800")
    print("7. Volver.")
    print(" ")
    modelo = int(input("Ingrese la opcion del modelo: "))

    if modelo == 7:
        salida = True
        # LimpiarPantalla()
        Productos()
    else:
        if modelo == 1:
            nombreModelo = "Campera Moscu"
            precio = 14000
        elif modelo == 2:
            nombreModelo = "Campera Morava"
            precio = 15100
        elif modelo == 3:
            nombreModelo = "Campera Cesana"
            precio = 16780
        elif modelo == 4:
            nombreModelo = "Campera Nuremberg"
            precio = 15900
        elif modelo == 5:
            nombreModelo = "Campera Banff"
            precio = 15320
        elif modelo == 6:
            nombreModelo = "Campera Rocker"
            precio = 16800

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
