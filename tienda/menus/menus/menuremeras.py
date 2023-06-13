# clase menu modelos buzos etcetc
from tienda.productos import Productos

class MenuRemeras:
    def __init__(self):
        self.modelo = 0
        self.cantidad = 0
        self.compra = 0
        self.agregarOpcion = 0
        self.precio = 0.0
        self.nombreModelo = ""
        self.salida = False

    def getModelo(self):
        return self.modelo

    def setModelo(self, modelo):
        self.modelo = modelo

    def getCantidad(self):
        return self.cantidad

    def setCantidad(self, cantidad):
        self.cantidad = cantidad

    def getCompra(self):
        return self.compra

    def setCompra(self, compra):
        self.compra = compra

    def getAgregarOpcion(self):
        return self.agregarOpcion

    def setAgregarOpcion(self, agregarOpcion):
        self.agregarOpcion = agregarOpcion

    def getPrecio(self):
        return self.precio

    def setPrecio(self, precio):
        self.precio = precio

    def getNombreModelo(self):
        return self.nombreModelo

    def setNombreModelo(self, nombreModelo):
        self.nombreModelo = nombreModelo

    def isSalida(self):
        return self.salida

    def setSalida(self, salida):
        self.salida = salida

    def menuRemeras(self, compraTotal, compraProductos):
        self.setAgregarOpcion(self.agregarOpcion)
        self.setCantidad(self.cantidad)
        self.setCompra(self.compra)
        self.setModelo(self.modelo)
        self.setNombreModelo(self.nombreModelo)
        self.setPrecio(self.precio)
        self.setSalida(self.salida)

        print("::..............................................................................................::")
        print("::                                         CATEGORIA REMERAS                                    ::")
        print("::                                        MODELOS DISPONIBLES                                   ::")
        print(
            "::..............................................................................................::\n")

        print("1. Remera Alzakaba: $10740")
        print("2. Remera Adventure: $10950")
        print("3. Remera Steeze: $10580")
        print("4. Remera Camber: $10000")
        print("5. Remera Pocket: $9550")
        print("6. Remera Sketch: $9200")
        print("7. Volver.\n")

        modelo = int(input("Ingrese opcion de modelo: "))

        if modelo == 1:
            self.nombreModelo = "Remera Alzakaba"
            self.precio = 10740
        elif modelo == 2:
            self.nombreModelo = "Remera Adventure"
            self.precio = 10950
        elif modelo == 3:
            self.nombreModelo = "Remera Steeze"
            self.precio = 10580
        elif modelo == 4:
            self.nombreModelo = "Remera Camber"
            self.precio = 10000
        elif modelo == 5:
            self.nombreModelo = "Remera Pocket"
            self.precio = 9550
        elif modelo == 6:
            self.nombreModelo = "Remera Sketch"
            self.precio = 9200
        elif modelo == 7:
            self.salida = True
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
                llamada = Productos()
                llamada.productos()
            else:
                print("Volviendo a la sección productos\n")
                print("Aguarde unos segundos...")
                llamada = Productos()
                llamada.productos()




