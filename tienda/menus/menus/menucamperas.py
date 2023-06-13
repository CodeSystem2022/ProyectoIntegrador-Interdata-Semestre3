from tienda.productos import Productos


class MenuCamperas:
    def init(self):
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

    def menuCamperas(self, compraTotal, compraProductos):
        self.setAgregarOpcion(self.agregarOpcion)
        self.setCantidad(self.cantidad)
        self.setCompra(self.compra)
        self.setModelo(self.modelo)
        self.setNombreModelo(self.nombreModelo)
        self.setPrecio(self.precio)
        self.setSalida(self.salida)

        print("::..............................................................................................::")
        print("::                                        CATEGORIA CAMPERAS                                    ::")
        print("::                                        MODELOS DISPONIBLES                                   ::")
        print(
            "::..............................................................................................::\n")

        print("1. Campera Moscú: $14000")
        print("2. Campera Morava: $15100")
        print("3. Campera Cesana: $16780")
        print("4. Campera Nuremberg: $15900")
        print("5. Campera Banff: $15320")
        print("6. Campera Rocker: $16800")
        print("7. Volver.")

        modelo = int(input("Ingrese opcion de modelo: "))

        if modelo == 1:
            self.nombreModelo = "Campera Moscú"
            self.precio = 14000
        elif modelo == 2:
            self.nombreModelo = "Campera Morava"
            self.precio = 15100
        elif modelo == 3:
            self.nombreModelo = "Campera Cesana"
            self.precio = 16780
        elif modelo == 4:
            self.nombreModelo = "Campera Nuremberg"
            self.precio = 15900
        elif modelo == 5:
            self.nombreModelo = "Campera Banff"
            self.precio = 15320
        elif modelo == 6:
            self.nombreModelo = "Campera Rocker"
            self.precio = 16800
        elif modelo == 7:
            self.salida = True
            # Limpiar Pantalla
            llamada = Productos()
            llamada.productos()

        if not self.salida:
            agregarOpcion = int(input("¿Desea añadir al carrito? [1. Si / 2. No]: "))

        if agregarOpcion == 1:
            cantidad = int(input("Cantidad de curvas: "))
            compraProductos += self.nombreModelo
            print(
                ".........................................................................................................")
            print(
                "::                                          AÑADIDO AL CARRITO                                        ::")
            print(
                ".........................................................................................................\n")
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