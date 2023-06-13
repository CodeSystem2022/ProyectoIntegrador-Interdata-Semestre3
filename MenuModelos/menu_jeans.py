import time


def menu_jeans(CompraTotal, CompraProductos):
    modelo = 0
    cantidad = 0
    precio = 0.0
    nombreModelo = ""
    agregarOpcion = 0
    salida = False
    compra = 0

    print("..................................................................................................")
    print("::                                         CATEGORIA JEANS                                      ::")
    print("::                                        MODELOS DISPONIBLES                                   ::")
    print("::..............................................................................................::")
    print("")

    print("1. Jeans Slim: $14700")
    print("2. Jeans Relaxed: $15650")
    print("3. Jeans Skinny: $14900")
    print("4. Jeans Baggy: $14000")
    print("5. Jeans Active: $14300")
    print("6. Jeans Classic: $13800")
    print("7. Volver.")
    print(" ")
    modelo = int(input("Ingrese la opcion del modelo: "))

    if modelo == 7:
        salida = True
        # LimpiarPantalla()
        Productos()
    else:
        if modelo == 1:
            nombreModelo = "Jeans Slim"
            precio = 14700
        elif modelo == 2:
            nombreModelo = "Jeans Relaxed"
            precio = 15650
        elif modelo == 3:
            nombreModelo = "Jeans Skinny"
            precio = 14900
        elif modelo == 4:
            nombreModelo = "Jeans Baggy"
            precio = 14000
        elif modelo == 5:
            nombreModelo = "Jeans Active"
            precio = 14300
        elif modelo == 6:
            nombreModelo = "Jeans Classic"
            precio = 13800

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