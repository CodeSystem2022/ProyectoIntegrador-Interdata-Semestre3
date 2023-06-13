from tienda.productos import Productos

class MenuTrajes:
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

    def menuTrajes(self, compraTotal, compraProductos):
        self.setAgregarOpcion(self.agregarOpcion)
        self.setCantidad(self.cantidad)
        self.setCompra(self.compra)
        self.setModelo(self.modelo)
        self.setNombreModelo(self.nombreModelo)
        self.setPrecio(self.precio)
        self.setSalida(self.salida)

        print("::..............................................................................................::")
        print("::                                         CATEGORIA TRAJES                                     ::")
        print("::                                        MODELOS DISPONIBLES                                   ::")
        print("::..............................................................................................::\n")

        print("1. Traje Pudong: $46740")
        print("2. Traje Quito: $45950")
        print("3. Traje Shangai: $49580")
        print("4. Traje Boston: $51800")
        print("5. Volver.\n")

        modelo = int(input("Ingrese opcion de modelo: "))

        if modelo == 1:
            self.nombreModelo = "Traje Pudong"
            self.precio = 46740
        elif modelo == 2:
            self.nombreModelo = "Traje Quito"
            self.precio = 45950
        elif modelo == 3:
            self.nombreModelo = "Traje Shangai"
            self.precio = 49580
        elif modelo == 4:
            self.nombreModelo = "Traje Boston"
            self.precio = 51800
        elif modelo == 5:
            self.salida = True
            llamada = Productos()
            llamada.productos()

        if not self.salida:
            agregarOpcion = int(input("¿Desea añadir al carrito? [1. Si / 2. No]: "))

        if agregarOpcion == 1:
            cantidad = int(input("Cantidad de curvas: "))
            compraProductos += self.nombreModelo
            print(".........................................................................................................")
            print("                                   :: ANIADIDO AL CARRITO ::                           ")
            print(".........................................................................................................\n")
            print("Producto: " + self.nombreModelo)
            print("Cantidad: " + str(cantidad))
            print("Precio $: " + str(self.precio))
            compra = int(self.precio * cantidad)
            compraTotal += compra
            print("Precio total $: " + str(compra))
        elif agregarOpcion == 2:
            print("Volviendo a la sección productos\n")
            print("Aguarde unos segundos...")
