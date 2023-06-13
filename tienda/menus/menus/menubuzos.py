from tienda.productos import Productos

class MenuBuzos:
    def __init__(self):
        self.modelo = 0
        self.cantidad = 0
        self.precio = 0.0
        self.nombreModelo = ""
        self.agregarOpcion = 0
        self.salida = False
        self.compra = 0

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getNombreModelo(self):
        return self.nombreModelo

    def setNombreModelo(self, nombreModelo):
        self.nombreModelo = nombreModelo

    def getAgregarOpcion(self):
        return self.agregarOpcion

    def setAgregarOpcion(self, agregarOpcion):
        self.agregarOpcion = agregarOpcion

    def isSalida(self):
        return self.salida

    def setSalida(self, salida):
        self.salida = salida

    def getCompra(self):
        return self.compra

    def setCompra(self, compra):
        self.compra = compra

    def menuBuzos(self, compraTotal, compraProductos):
        self.setAgregarOpcion(self.agregarOpcion)
        self.setCantidad(self.cantidad)
        self.setCompra(self.compra)
        self.setModelo(self.modelo)
        self.setNombreModelo(self.nombreModelo)
        self.setPrecio(self.precio)
        self.setSalida(self.salida)

        print("::..............................................................................................::")
        print("::                                         CATEGORIA BUZOS                                      ::")
        print("::                                        MODELOS DISPONIBLES                                   ::")
        print("::..............................................................................................::\n")

        print("1. Buzo Essential: $12740.")
        print("2. Buzo Hoodie: $11950.")
        print("3. Buzo Shadow: $12580.")
        print("4. Buzo Flock: $13000.")
        print("5. Buzo Saona: $13320.")
        print("6. Buzo Lorain: $12800.")
        print("7. Volver.\n")

        modelo = int(input("Ingrese opcion de modelo: "))

        if modelo == 1:
            self.nombreModelo = "Buzo Essential"
            self.precio = 12740
        elif modelo == 2:
            self.nombreModelo = "Buzo Hoodie"
            self.precio = 11950
        elif modelo == 3:
            self.nombreModelo = "Buzo Shadow"
            self.precio = 12580
        elif modelo == 4:
            self.nombreModelo = "Buzo Flock"
            self.precio = 13000
        elif modelo == 5:
            self.nombreModelo = "Buzo Saona"
            self.precio = 13320
        elif modelo == 6:
            self.nombreModelo = "Buzo Lorain"
            self.precio = 12800
        elif modelo == 7:
            self.salida = True
            llamada = Productos()
            llamada.productos()

        if not self.salida:
            agregarOpcion = int(input("¿Desea añadir al carrito? [1. Si / 2. No]: "))

        if agregarOpcion == 1:
            cantidad = int(input("Cantidad de curvas: "))
            compraProductos += self.nombreModelo
            print("........................................................................................................")
            print("::                                          AÑADIDO AL CARRITO                                        ::")
            print("........................................................................................................\n")
            print("Producto: " + self.nombreModelo)
            print("Cantidad: " + str(cantidad))
            print("Precio $: " + str(self.precio))
            compra = int(self.precio * cantidad)
            compraTotal += compra
            print("Precio total $: " + str(compra))
            # Esperar 5 segundos
            # Limpiar pantalla
        elif agregarOpcion == 2:
            print("Volviendo a la sección productos\n")
            # Esperar 1/2 segundo
            print("Aguarde unos segundos...")
            llamada = Productos()
            llamada.productos()
