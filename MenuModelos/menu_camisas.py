import time


def menu_camisas(CompraTotal, CompraProductos):
    modelo = 0
    cantidad = 0
    precio = 0.0
    nombreModelo = ""
    agregarOpcion = 0
    salida = False
    compra = 0

    print("..................................................................................................")
    print("::                                         CATEGORIA CAMISAS                                    ::")
    print("::                                        MODELOS DISPONIBLES                                   ::")
    print("::..............................................................................................::")
    print("")

    print("1. Camisa Hefei: $30740")
    print("2. Camisa Pekin:$25950")
    print("3. Camisa Canton: $28580")
    print("4. Camisa Nankin: $29000")
    print("5. Camisa Hangzhou: $24050")
    print("6. Camisa Quanzhou: $28200")
    print("7. Volver.")
    print(" ")
    modelo = int(input("Ingrese la opcion del modelo: "))

    if modelo == 7:
        salida = True
        # LimpiarPantalla()
        Productos()
    else:
        if modelo == 1:
            nombreModelo = "Camisa Hefei"
            precio = 30740
        elif modelo == 2:
            nombreModelo = "Camisa Pekin"
            precio = 25950
        elif modelo == 3:
            nombreModelo = "Camisa Canton"
            precio = 28580
        elif modelo == 4:
            nombreModelo = "Camisa Nankin"
            precio = 29000
        elif modelo == 5:
            nombreModelo = "Camisa Hangzhou"
            precio = 24050
        elif modelo == 6:
            nombreModelo = "Camisa Quanzhou"
            precio = 28200

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