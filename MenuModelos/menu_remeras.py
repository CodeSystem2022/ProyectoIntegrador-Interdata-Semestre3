import time

def menu_remeras(CompraTotal, CompraProductos):
    modelo = 0
    cantidad = 0
    precio = 0.0
    nombreModelo = ""
    agregarOpcion = 0
    salida = False
    compra = 0
    
    
    print("..................................................................................................")
    print("::                                         CATEGORIA REMERAS                                    ::")
    print("::                                        MODELOS DISPONIBLES                                   ::")
    print("::..............................................................................................::")
    print("")
    
    print("1. Remera Alzakaba: $10740")
    print("2. Remera Adventure: $10950")
    print("3. Remera Steeze: $10580")
    print("4. Remera Camber: $10000")
    print("5. Remera Pocket: $9550")
    print("6. Remera Sketch: $9200")
    print("7. Volver.")
    print(" ")
    modelo = int(input("Ingrese la opcion del modelo: "))
    
    if modelo == 7:
        salida = True
        #LimpiarPantalla()
        Productos()
    else:
        if modelo == 1:
            nombreModelo = "Remera Alzakaba"
            precio = 10740
        elif modelo == 2:
            nombreModelo = "Remera Adventure"
            precio = 10950
        elif modelo == 3:
            nombreModelo = "Remera Steeze"
            precio = 10580
        elif modelo == 4:
            nombreModelo = "Remera Camber"
            precio = 10000
        elif modelo == 5:
            nombreModelo = "Remera Pocket"
            precio = 9550
        elif modelo == 6:
            nombreModelo = "Remera Sketch"
            precio = 9200
        
        if not salida:
            print("¿Aniadir al carrito? 1.Si -- 2.No: ")
            agregarOpcion = int(input())
        
        if agregarOpcion == 1:
            print("Cantidad: ", end="")
            cantidad = int(input())
            CompraProductos += nombreModelo
            #LimpiarPantalla()
            
            print(".........................................................................................................")
            print("                                   :: AÑADIDO AL CARRITO ::                           ")
            print(".........................................................................................................")
            print("Producto añadido al carrito: ", nombreModelo)
            print("Cantidad: ", cantidad)
            print("Precio por curva $: ", precio)
            Compra = precio * cantidad
            CompraTotal += (precio * cantidad)
            print("Precio total de lo añadido $: ", Compra)
            time.sleep(5)
            #LimpiarPantalla()
        elif agregarOpcion == 2:
            print("Volviendo a la sección productos")
            time.sleep(0.5)
            print("")
            print("Aguarde unos segundos ....")
            time.sleep(2)
            #LimpiarPantalla()
