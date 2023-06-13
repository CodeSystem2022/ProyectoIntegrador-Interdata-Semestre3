from pago.metodopago import MetodoPago


class Productos:
    def __init__(self):
        self.opcion = 0
        self.compraTotal = 0.0
        self.compraProductosR = ""
        self.compraProductosB = ""
        self.compraProductosC = ""
        self.compraProductosJ = ""
        self.compraProductosP = ""
        self.compraProductosTra = ""
        self.compraProductosCa = ""
        self.salir = False

    def getOpcion(self):
        return self.opcion

    def setOpcion(self, opcion):
        self.opcion = opcion

    def getCompraTotal(self):
        return self.compraTotal

    def setCompraTotal(self, compraTotal):
        self.compraTotal = compraTotal

    def getCompraProductosR(self):
        return self.compraProductosR

    def setCompraProductosR(self, compraProductosR):
        self.compraProductosR = compraProductosR

    def getCompraProductosB(self):
        return self.compraProductosB

    def setCompraProductosB(self, compraProductosB):
        self.compraProductosB = compraProductosB

    def getCompraProductosC(self):
        return self.compraProductosC

    def setCompraProductosC(self, compraProductosC):
        self.compraProductosC = compraProductosC

    def getCompraProductosJ(self):
        return self.compraProductosJ

    def setCompraProductosJ(self, compraProductosJ):
        self.compraProductosJ = compraProductosJ

    def getCompraProductosP(self):
        return self.compraProductosP

    def setCompraProductosP(self, compraProductosP):
        self.compraProductosP = compraProductosP

    def getCompraProductosTra(self):
        return self.compraProductosTra

    def setCompraProductosTra(self, compraProductosTra):
        self.compraProductosTra = compraProductosTra

    def getCompraProductosCa(self):
        return self.compraProductosCa

    def setCompraProductosCa(self, compraProductosCa):
        self.compraProductosCa = compraProductosCa

    def isSalir(self):
        return self.salir

    def setSalir(self, salir):
        self.salir = salir

    def productos(self):
        import menus
        remeras = menus.MenuRemeras()
        buzos = menus.MenuBuzos()
        camperas = menus.MenuCamperas()
        jeans = menus.MenuJeans()
        pantalones = menus.MenuPantalones()
        camisas = menus.MenuCamisas()
        trajes = menus.MenuTrajes()

        self.setOpcion(self.opcion)
        self.setCompraProductosB(self.compraProductosB)
        self.setCompraProductosC(self.compraProductosC)
        self.setCompraProductosCa(self.compraProductosCa)
        self.setCompraProductosJ(self.compraProductosJ)
        self.setCompraProductosP(self.compraProductosP)
        self.setCompraProductosR(self.compraProductosR)
        self.setCompraProductosTra(self.compraProductosTra)
        self.setCompraTotal(self.compraTotal)
        self.setSalir(self.salir)

        while True:
            print(
                ".......................................................................................................................")
            print(
                "::                                                         CATEGORIAS                                                ::")
            print(
                "::                                             COLECCION OTONIO - INVIERNO 2022                                        ::")
            print(
                "::...................................................................................................................::\n")

            print("1.Remeras")
            print("2.Buzos")
            print("3.Camperas")
            print("4.Jeans")
            print("5.Pantalones Joggin")
            print("6.Camisas")
            print("7.Trajes")
            print("8.Ver carrito de compras")
            print("9.Salir de la cuenta\n")

            opcion = int(input("Ingresa la categoria ingresada: "))

            if opcion == 1:
                remeras.menuRemeras(self.compraTotal, self.compraProductosR)
            elif opcion == 2:
                buzos.menuBuzos(self.compraTotal, self.compraProductosB)
            elif opcion == 3:
                camperas.menuCamperas(self.compraTotal, self.compraProductosC)
            elif opcion == 4:
                jeans.menuJeans(self.compraTotal, self.compraProductosJ)
            elif opcion == 5:
                pantalones.menuPantalones(self.compraTotal, self.compraProductosP)
            elif opcion == 6:
                camisas.menuCamisas(self.compraTotal, self.compraProductosCa)
            elif opcion == 7:
                trajes.menuTrajes(self.compraTotal, self.compraProductosTra)
            elif opcion == 8:
                print(
                    "::....................................................................................................................................................::")
                print(
                    "::                                                          :: CARRITO DE COMPRAS ::                                                                   ::")
                print(
                    "::....................................................................................................................................................::\n")
                print("Los productosymenus agregados al carrito son: ")
                if remeras.getNombreModelo() != None:
                    print(remeras.getNombreModelo())
                if buzos.getNombreModelo() != None:
                    print(buzos.getNombreModelo())
                if pantalones.getNombreModelo() != None:
                    print(pantalones.getNombreModelo())
                if camisas.getNombreModelo() != None:
                    print(camisas.getNombreModelo())
                if camperas.getNombreModelo() != None:
                    print(camperas.getNombreModelo())
                if trajes.getNombreModelo() != None:
                    print(trajes.getNombreModelo())
                if jeans.getNombreModelo() != None:
                    print(jeans.getNombreModelo())
                compraTotal = (
                        remeras.getCompra()
                        + buzos.getCompra()
                        + pantalones.getCompra()
                        + camisas.getCompra()
                        + camperas.getCompra()
                        + trajes.getCompra()
                        + jeans.getCompra()
                )
                print("El monto total es: " + str(compraTotal))
                pago = MetodoPago()
                pago.metodoPago(compraTotal)
            elif opcion == 9:
                self.salir = True
                break
