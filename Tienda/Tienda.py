
compraTotal = 0
monto = 0           #VARIABLES GLOBALES
cantidad = 0
item = ""
numero_carrito = 0
booleano = True

class InicioTienda:
    def __init__(self, conexion):
        self.conexion = conexion
        self.cursor = self.conexion.cursor()

    def inicio_tienda(self):
        while True:
            print(
                "..................................................................................................................")
            print(
                "::                                                   INTERDATA                                                  ::")
            print(
                "::                                        TIENDA MAYORISTA DE ROPA PARA HOMBRE                                  ::")
            print(
                "::..............................................................................................................::")
            print(" ")
            print(" Somos una tienda mayorista vendemos por curva de 5 unidades, talles y colores sin eleccion")
            print(" ")
            print("1. Iniciar sesión")
            print("2. Registrar nuevo usuario")
            print("3. Salir de la página")
            opcion = input("\nIngrese una opción: ")

            if opcion == "1":
                self.iniciar_sesion()
            elif opcion == "2":
                self.registrar_usuario()
            elif opcion == "3":
                print("\nSaliendo de la página...")
                print("¡Gracias por visitarnos!\n")
                print("                          _   _              _           ____                      _                 ")
                print("                         | | | |  __ _  ___ | |_  __ _  |  _ \  _ __  ___   _ __  | |_  ___          ")
                print("                         | |_| | / _` |/ __|| __|/ _` | | |_) || '__|/ _ \ | '_ \ | __|/ _ \         ")
                print("                         |  _  || (_| |\__ \| |_| (_| | |  __/ | |  | (_) || | | || |_| (_) |        ")
                print("                         |_| |_| \__,_||___/ \__|\__,_| |_|    |_|   \___/ |_| |_| \__|\___/         ")

                break
            else:
                print("La opción ingresada es incorrecta. Por favor, inténtelo nuevamente.")

        self.cursor.close()
        self.conexion.close()
        exit()


    def iniciar_sesion(self):
        print("\n.........................................................................................................")
        print("::                                            MI CUENTA                                                ::")
        print("::.....................................................................................................::")
                
        usuario = input("\nNombre de usuario: ")
        clave = input("Contraseña: ")

        if self.verificar_credenciales(usuario, clave):
            print("")
            print("Inicio de sesión exitoso")
            self.mostrar_categorias()
            
        else:
            print("Los datos ingresados son incorrectos")
            print("Por favor, verifique el nombre de usuario y contraseña")

    def verificar_credenciales(self, usuario, clave):
        sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
        self.cursor.execute('SELECT * FROM usuarios WHERE usuario=%s AND clave=%s', (usuario, clave))
        usuario = self.cursor.fetchone()
        return bool(usuario)

    def registrar_usuario(self):
        print(".........................................................................................................")
        print("::                                            MI CUENTA                                                ::")
        print("::                                      Creando un nuevo usuario                                       ::")
        print("::.....................................................................................................::")
        print("")
        usuario = input("Nombre de usuario: ")
        clave = input("Contraseña: ")
        clave2 = input("Repita la contraseña: ")

        if clave == clave2:
            if self.crear_usuario(usuario, clave):

                print("\n¡Su cuenta ha sido creada con éxito!")
                print("Estamos redirigiéndolo...")

                self.mostrar_categorias()
            else:
                print("Ocurrió un error al crear la cuenta. Por favor, inténtelo nuevamente.")
        else:
            print("Las contraseñas ingresadas no coinciden")


    def crear_usuario(self, usuario, clave):
        try:
            self.cursor.execute('INSERT INTO usuarios (usuario, clave) VALUES (%s, %s)', (usuario, clave))
            self.conexion.commit()
            return True
        except Exception as e:
            print("Ocurrió un error al crear el usuario:", str(e))
            return False

    def mostrar_categorias(self): #Metodo que solo muestra las categorias

        print(".......................................................................................................................")
        print("::                                                         CATEGORIAS                                                ::")
        print("::                                             COLECCION OTOÑO - INVIERNO 2023                                       ::")
        print("::...................................................................................................................::\n")

        print("1) Remeras") 
        print("2) Buzos")
        print("3) Camperas")
        print("4) Jeans")
        print("5) Pantalones Jogging")
        print("6) Camisas")
        print("7) Trajes")
        print("8) Ver carrito de compras")
        print("9) Salir de la cuenta\n")
       
        return self.elegir_categoria()    
 

    def elegir_categoria(self): # Recibe opción del usuario y devuelve la categoria deseada
        opcion = int(input("Ingrese una opción: "))
        case1= lambda : "Remera"                
        case2= lambda : "Buzo"                  # Creamos las funciones lambdas(cortas) 
        case3= lambda : "Campera"               # segun cada opcion
        case4= lambda : "Jean"
        case5= lambda : "Jogging"
        case6= lambda : "Camisa"
        case7= lambda : "Traje"
        case8= lambda : self.ver_carrito()
        case9= lambda : self.inicio_tienda() 
        default = lambda: self.mostrar_categorias()
        switch = {1:case1,2:case2,3:case3,4:case4,5:case5,6:case6,7:case7,8:case8,9:case9} 

        return self.mostrar_productos(switch.get(opcion,default)())


    def mostrar_productos(self,categoria): # Muestra N cantidad de productos

        self.cursor.execute(f"SELECT name FROM productos WHERE type = '{categoria}'")
        nombres = self.cursor.fetchall() #Se guardan lo nombres
        self.cursor.execute(f"SELECT price FROM productos WHERE type = '{categoria}'")
        precios = self.cursor.fetchall() #Se guardan los precios
        i=1

        print("..................................................................................................")
        print(f"::                                        CATEGORIA {categoria.upper()}S                               \t::")
        print("::                                        MODELOS DISPONIBLES                                   ::")
        print("::..............................................................................................::")
        print("")

        for nombre,precio in zip(nombres,precios):
            impresion_P = precio[0]    
            impresion_N = nombre[0]
            print(f"{i}) {impresion_N} ${impresion_P}")
            i+=1

        print(f"{i}) Volver atras")    

        def elegir_producto(categoria1): # Toma la opcion del usuario
            nonlocal i
            global compraTotal
            global monto
            global cantidad
            global item
            global numero_carrito
            opcion = int(input("\nIngrese una opción: "))
            
            if opcion >= i:  #Condicional que en caso de que la opcion no sea un producto vuelve a categorias
                
                return self.mostrar_categorias()
                
            cantidad = int(input("Cantidad: "))
            self.cursor.execute(f"SELECT price FROM productos WHERE type = '{categoria1}'")
            precios = self.cursor.fetchall()
            precio = precios[opcion-1]  
            monto= precio[0]*cantidad   #Guarda el monto
            self.cursor.execute(f"SELECT name FROM productos WHERE type = '{categoria1}'")
            items = self.cursor.fetchall()
            item1 = items[opcion-1]
            item = item1[0]             #Guarda el nombre del item
            
            
            print("¿Desea agregar al carrito?")
            print("1) Si")
            print("2) No")
            confirmacion = int(input("Ingrese la opción seleccionada: "))
            if confirmacion != 1: 
                
                return self.mostrar_productos(categoria1)

            compraTotal +=monto
            self.agregar_carrito(categoria1)

            return self.mostrar_productos(categoria1)

                        
        return elegir_producto(categoria)
    
    
    def agregar_carrito(self,categoria2): #Muestra producto agregado y inserta en la base
            global cantidad
            global monto
            global item
            global compraTotal
            global numero_carrito
            global booleano
                

            self.cursor.execute(f'INSERT INTO carrito ( nombre, cantidad, precio) VALUES (\'{item}\',{cantidad},{monto})')
            self.conexion.commit()
            if booleano:
                booleano=False
                self.cursor.execute("SELECT numero FROM carrito ORDER BY numero DESC LIMIT 1")
                numero_carrito = self.cursor.fetchone()
            
            print("\n..................................................................................................")
            print("::                                 PRODUCTO AÑADIDO AL CARRITO                                  ::")
            print("..................................................................................................")
            print("")
            print(f"Agregado: {categoria2.upper()} {item.upper()}")
            print(f"Cantidad: {cantidad}")
            print(f"Monto añadido: $ {monto}")
            print(f"Total del carrito: ${compraTotal}")
            print("..................................................................................................")
            print("")
            print("")
    def ver_carrito(self):
        global compraTotal

        self.cursor.execute(f"SELECT nombre FROM carrito OFFSET {numero_carrito[0]-1}")
        nombres_c = self.cursor.fetchall()
        self.cursor.execute(f"SELECT precio FROM carrito OFFSET {numero_carrito[0]-1}")
        montos_c = self.cursor.fetchall() 
        self.cursor.execute(f"SELECT cantidad FROM carrito OFFSET {numero_carrito[0]-1}")
        cantidades_c = self.cursor.fetchall() 


        print("..................................................................................................")
        print("::                                         CARRITO DE COMPRAS                                   ::")
        print("::..............................................................................................::")
        print("::               Producto          |           Cantidad             |           Total           ::")
        print("::..............................................................................................::")

        for nombre_c,monto_c,cantidad_c in zip(nombres_c,montos_c, cantidades_c):
            impresion_m = monto_c[0]    
            impresion_n = nombre_c[0]
            impresion_c = cantidad_c[0]
            print(f"::\t\t{impresion_n}                           {impresion_c}                            ${impresion_m}     ")

        print("..................................................................................................")
        print(f":: TOTAL DE LA COMPRA: ${compraTotal}                                                             ")
        print("..................................................................................................")
        print("")

        print(" ¿Desea finalizar la compra?")
        print("\n1) Proceder al pago")
        print("2) Volver al menú")
        print("")
        
        opcion = int(input("Ingresa una opción: "))

        if opcion == 1:
            return self.metodo_pago(compraTotal) # ACA AGREGAR METODOS DE PAGO
        else:
            return self.mostrar_categorias()


    def metodo_pago(self,compraTotal):
        
        print("::..............................................................................................::")
        print("::                                         MÉTODOS DE PAGOS                                     ::")
        print("::..............................................................................................::\n")

        print("1) Transferencia bancaria")
        print("2) Tarjeta de Débito")
        print("3) Tarjeta de Crédito")
        print("4) Mercado Pago")
        print("5) Volver atrás\n")

        opcionPago = int(input("Ingrese la opción de método de pago: "))
        if opcionPago == 1:
            print("::..............................................................................................::")
            print("::                                         TRANSFERENCIA BANCARIA                               ::")
            print("::..............................................................................................::\n")
            print("En pagos por transferencia 10 de descuento")
            print("ALIAS: Interdata.tienda")
            print("CBU: 000004377328742785")
            print(f"Total de la compra: $ {compraTotal}")
            print("\nAplicando el descuento del 10 %")
            compraTotalneto = compraTotal-compraTotal * 0.05
            print(f"Importe a pagar: ${compraTotalneto}")
            
            print("\n................................................................................................")
            print(":                                        ¿Desea realizar el pago?                               :")
            print(":...............................................................................................:")
            print(" 1) Si                                                                                         ")
            print(" 2) No                                                                                         ")

            respuesta = int(input("\nIngrese una opción: "))

            if respuesta == 1:
                    self.cursor.execute('INSERT INTO pagos (monto, metodo) VALUES (%s, %s)', (compraTotalneto, 'Transferencia bancaria'))
                    self.conexion.commit()
                    print("Estamos comprobando su pago, espere unos segundos..")
                    print("Su pago fue realizado con éxito\n")
                    print("¡Gracias por su compra!\n")
                    return self.post_pago()
                    
            else:
                self.metodo_pago(compraTotal)

        elif opcionPago == 2:
            print("::..............................................................................................::")
            print("::                                         TARJETA DE DÉBITO                                    ::")
            print("::..............................................................................................::\n")
            print("\nLos pagos con débito no tienen descuento ni recargo")
            print(f"Importe a pagar: ${compraTotal}")
            print("\n................................................................................................")
            print(":                                        ¿Desea realizar el pago?                               :")
            print(":...............................................................................................:")
            print(" 1) Si                                                                                         ")
            print(" 2) No                                                                                         ")


            respuesta = int(input("\nIngrese una opción: "))

            if respuesta == 1:
                self.cursor.execute('INSERT INTO pagos (monto, metodo) VALUES (%s, %s)', (compraTotal, 'Tarjeta de débito'))
                self.conexion.commit()
                print("Ingrese los datos de la tarjeta")
                print("Número de tarjeta: ", end="")
                numeroTarjeta = int(input())
                print("Titular: ", end="")
                tt = input()
                print("Año de vencimiento: ", end="")
                fv = int(input())
                print("CVV: ", end="")
                cvv = int(input())
                print("Su pago fue realizado con éxito")
                print("¡Gracias por su compra!\n")
                return self.post_pago()
            else:
                self.metodo_pago(compraTotal)

        elif opcionPago == 3:
            print("::..............................................................................................::")
            print("::                                         TARJETA DE CRÉDITO                                   ::")
            print("::..............................................................................................::\n")
            print("Las tarjetas de crédito poseen un recargo del 25%\n")
            print("Importe Bruto: $", compraTotal)
            print("\nAplicando el recargo de 25 %")
            compraTotalneto = compraTotal+compraTotal * 0.25
            print("Importe neto a pagar: $", compraTotalneto)
            print("\n................................................................................................")
            print(":                                        ¿Desea realizar el pago?                               :")
            print(":...............................................................................................:")
            print(" 1) Si                                                                                         ")
            print(" 2) No                                                                                         ")

            respuesta = int(input("\nIngrese una opción: "))

            if respuesta == 1:
                self.cursor.execute('INSERT INTO pagos (monto, metodo) VALUES (%s, %s)', (compraTotalneto, 'Tarjeta de crédito'))
                self.conexion.commit()
                print("Ingrese los datos de la tarjeta")
                print("Número de tarjeta: ", end="")
                numeroTarjeta = int(input())
                print("Titular: ", end="")
                tt = input()
                print("Año de vencimiento: ", end="")
                fv = int(input())
                print("CVV: ", end="")
                cvv = int(input())
                print("Su pago fue realizado con éxito")
                print("¡Gracias por su compra!\n")
                return self.post_pago()
            else:
                self.metodo_pago(compraTotal)

        elif opcionPago == 4:
            print("::..............................................................................................::")
            print("::                                         MERCADO PAGO                                         ::")
            print("::..............................................................................................::\n")
            print("En pagos por Mercado Pago 5% de descuento")
            print("ALIAS: Interdata.mp")
            print("CBU: 00000238298729357")
            print("Importe bruto: ", compraTotal)
            print("\nAplicando el descuento")
            compraTotalneto = compraTotal-compraTotal * 0.05
            print("\nImporte neto a pagar: ", compraTotalneto)

            print("\n................................................................................................")
            print(":                                        ¿Desea realizar el pago?                               :")
            print(":...............................................................................................:")
            print(" 1) Si                                                                                         ")
            print(" 2) No                                                                                         ")

            respuesta = int(input("\nIngrese una opción: "))

            if respuesta == 1:
                self.cursor.execute('INSERT INTO pagos (monto, metodo) VALUES (%s, %s)', (compraTotalneto, 'Mercado Pago'))
                self.conexion.commit()                
                print("Su pago fue realizado con éxito")
                print("¡Gracias por su compra!\n")
                return self.post_pago()
            else:
                self.metodo_pago(compraTotal)

        elif opcionPago == 5:
            print("Volviendo a la sección productos")
            print("\nAguarde unos segundos...")
            self.mostrar_categorias()

        else:
            print("La opción ingresada no es válida")
            print("Por favor intentelo nuevamente")

    def post_pago(self):
        global compraTotal
        global monto            #VARIABLES GLOBALES
        global cantidad 
        global item 
        global numero_carrito 
        global booleano 

        compraTotal = 0
        monto = 0           
        cantidad = 0            #RESETEAMOS TODAS LAS VARIABLES GLOBALES
        item = ""
        numero_carrito = 0
        booleano = True

        print(" 1) Volver a la tienda                                        ")
        print(" 2) Salir del programa                                        ")
      
        opcion =  int(input("\nIngrese una opción:"))
        if opcion == 1:
            return self.mostrar_categorias()
        elif opcion ==2:
            print("                          _   _              _           ____                      _                 ")
            print("                         | | | |  __ _  ___ | |_  __ _  |  _ \  _ __  ___   _ __  | |_  ___          ")
            print("                         | |_| | / _` |/ __|| __|/ _` | | |_) || '__|/ _ \ | '_ \ | __|/ _ \         ")
            print("                         |  _  || (_| |\__ \| |_| (_| | |  __/ | |  | (_) || | | || |_| (_) |        ")
            print("                         |_| |_| \__,_||___/ \__|\__,_| |_|    |_|   \___/ |_| |_| \__|\___/         ")
            return exit()
        
        return self.post_pago()
        
