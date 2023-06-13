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

class Productos:
    import menus
    def __init__(self):
        self.compra_productos_b = []
        self.compra_productos_c = []
        self.compra_productos_ca = []
        self.compra_productos_j = []
        self.compra_productos_p = []
        self.compra_productos_r = []
        self.compra_productos_tra = []
        self.compra_total = 0
        self.salir = False

    def set_opcion(self, opcion):
        self.opcion = opcion

    def menu_principal(self):
        print(".......................................................................................................................")
        print("::                                                         CATEGORIAS                                                ::")
        print("::                                             COLECCION OTONIO - INVIERNO 2022                                        ::")
        print("::...................................................................................................................::\n")

        print("1.Remeras")
        print("2.Buzos")
        print("3.Camperas")
        print("4.Jeans")
        print("5.Pantalones Joggin")
        print("6.Camisas")
        print("7.Trajes")
        print("8.Ver carrito de compras")
        print("9.Salir de la cuenta\n")

    def menu_compras(self):
        remeras = menus.MenuRemeras()
        buzos = menus.MenuBuzos()
        camperas = menus.MenuCamperas()
        jeans = menus.MenuJeans()
        pantalones = menus.MenuPantalones()
        camisas = menus.MenuCamisas()
        trajes = menus.MenuTrajes()

        if self.opcion == 1:
            remeras.menuRemeras(self.compra_total, self.compra_productos_r)
        elif self.opcion == 2:
            buzos.menuBuzos(self.compra_total, self.compra_productos_b)
        elif self.opcion == 3:
            camperas.menuCamperas(self.compra_total, self.compra_productos_c)
        elif self.opcion == 4:
            jeans.menuJeans(self.compra_total, self.compra_productos_j)
        elif self.opcion == 5:
            pantalones.menuPantalones(self.compra_total, self.compra_productos_p)
        elif self.opcion == 6:
            camisas.menuCamisas(self.compra_total, self.compra_productos_ca)
        elif self.opcion == 7:
            trajes.menuTrajes(self.compra_total, self.compra_productos_tra)

    def menu_carrito(self):
        print("::....................................................................................................................................................::")
        print("::                                                          :: CARRITO DE COMPRAS ::                                                                   ::")
        print("::....................................................................................................................................................::\n")
        print("Los productos y menus agregados al carrito son: ")
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
            compra_total = (remeras.getCompra() + buzos.getCompra() + pantalones.getCompra() + camisas.getCompra() + camperas.getCompra() + trajes.getCompra())
            print("El monto total es: " + str(compra_total))
            pago = MetodoPago()
            pago.metodoPago(compra_total)
        elif opcion == 9:
            self.salir = True
            break

