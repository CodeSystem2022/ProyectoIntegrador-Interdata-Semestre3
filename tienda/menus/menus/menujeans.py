from tienda.productos import Productos

class MenuJeans:
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

    def menuJeans(self, compraTotal, compraProductos):
        self.setAgregarOpcion(self.agregarOpcion)
        self.setCantidad(self.cantidad)
        self.setCompra(self.compra)
        self.setModelo(self.modelo)
        self.setNombreModelo(self.nombreModelo)
        self.setPrecio(self.precio)
        self.setSalida(self.salida)

        print("::..............................................................................................::")
        print("::                                         CATEGORIA JEANS                                      ::")
        print("::                                        MODELOS DISPONIBLES                                   ::")
        print("::..............................................................................................::\n")

        print("1. Jeans Slim: $14700")
        print("2. Jeans Relaxed: $15650")
        print("3. Jeans Skinny: $14900")
        print("4. Jeans Baggy: $14000")
        print("5. Jeans Active: $14300")
        print("6. Jeans Classic: $13800")
        print("7. Volver.\n")

        modelo = int(input("Ingrese opcion modelo: "))

        if modelo == 1:
            self.nombreModelo = "Jeans Modelo Slim"
            self.precio = 14700
        elif modelo == 2:
            self.nombreModelo = "Jeans Relaxed"
            self.precio = 15650
        elif modelo == 3:
            self.nombreModelo = "Jeans Skinny"
            self.precio = 14900
        elif modelo == 4:
            self.nombreModelo = "Jeans Baggy"
            self.precio = 14000
        elif modelo == 5:
            self.nombreModelo = "Jeans Active"
            self.precio = 14300
        elif modelo == 6:
            self.nombreModelo = "Jeans Classic"
            self.precio = 13800
        elif modelo == 7:
            self.salida = True
            llamada = Productos()
            llamada.productos()

        if not self.salida:
            agregarOpcion = int(input("¿Desea añadir al carrito? [1. Si / 2. No]: "))

        if agregarOpcion == 1:
            cantidad = int(input("Cantidad de curvas: "))
            compraProductos += self.nombreModelo
            print(".........................................................................................................")
            print("::                                          AÑADIDO AL CARRITO                                        ::")
            print(".........................................................................................................\n")
            print("Producto: " + self.nombreModelo)
            print("Cantidad: " + str(cantidad))
            print("Precio $: " + str(self.precio))
            compra = int(self.precio * cantidad)
            compraTotal += compra
            print("Precio total $: " + str(compra))
        elif agregarOpcion == 2:
            print("Volviendo a la seccion productos\n")
            # Esperar 1/2 segundo
            print("Aguarde unos segundos...")
            llamada = Productos()
            llamada.productos()
