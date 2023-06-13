from tienda.productos import Productos


class MetodoPago:
    def __init__(self):
        self.opcionPago = 0
        self.respuesta = 0
        self.numeroTarjeta = 0
        self.cvv = 0
        self.fv = 0
        self.tt = ""
        self.procederPago = 0
        self.salida = False

    def getOpcionPago(self):
        return self.opcionPago

    def setOpcionPago(self, opcionPago):
        self.opcionPago = opcionPago

    def getRespuesta(self):
        return self.respuesta

    def setRespuesta(self, respuesta):
        self.respuesta = respuesta

    def getNumeroTarjeta(self):
        return self.numeroTarjeta

    def setNumeroTarjeta(self, numeroTarjeta):
        self.numeroTarjeta = numeroTarjeta

    def getCvv(self):
        return self.cvv

    def setCvv(self, cvv):
        self.cvv = cvv

    def getFv(self):
        return self.fv

    def setFv(self, fv):
        self.fv = fv

    def getTt(self):
        return self.tt

    def setTt(self, tt):
        self.tt = tt

    def getProcederPago(self):
        return self.procederPago

    def setProcederPago(self, procederPago):
        self.procederPago = procederPago

    def isSalida(self):
        return self.salida

    def setSalida(self, salida):
        self.salida = salida

    def metodoPago(self, compraTotal):
        self.setCvv(self.cvv)
        self.setFv(self.fv)
        self.setNumeroTarjeta(self.numeroTarjeta)
        self.setOpcionPago(self.opcionPago)
        self.setProcederPago(self.procederPago)
        self.setRespuesta(self.respuesta)
        self.setSalida(self.salida)
        self.setTt(self.tt)

        print("¿Desea proceder al pago? [1. Si / 2. No]: ", end="")
        procederPago = int(input())

        if procederPago != 1:
            llamada = Productos()
            llamada.productos()

        print("::..............................................................................................::")
        print("::                                         MÉTODOS DE PAGOS                                     ::")
        print("::..............................................................................................::\n")

        print("1. Transferencia bancaria")
        print("2. Tarjeta de Débito")
        print("3. Tarjeta de Crédito")
        print("4. Mercado Pago")
        print("5. Volver atrás\n")

        print("Ingrese la opción de método de pago: ", end="")
        opcionPago = int(input())

        if opcionPago == 1:
            print("::..............................................................................................::")
            print("::                                         TRANSFERENCIA BANCARIA                               ::")
            print("::..............................................................................................::\n")
            print("En pagos por transferencia 10% de descuento")
            print("ALIAS: Interdata.tienda")
            print("CBU: 000004377328742785")
            print("\nImporte Bruto: ", compraTotal)
            print("Aplicando el descuento del 10%")
            compraTotal -= compraTotal * 0.10
            print("\nImporte Neto a pagar: ", compraTotal)
            print("¿Desea realizar el pago? [1. Si / 2. No]: ", end="")
            respuesta = int(input())

            if respuesta == 1:
                print("Estamos comprobando su pago, espere unos segundos..")
                print("Su pago fue realizado con éxito\n")
                print("¡Gracias por su compra!\n")
            else:
                metodoP = MetodoPago()
                metodoP.metodoPago(compraTotal)

        elif opcionPago == 2:
            print("::..............................................................................................::")
            print("::                                         TARJETA DE DÉBITO                                    ::")
            print("::..............................................................................................::\n")
            print("Los pagos con débito no tienen descuento ni recargo")
            print("Importe a pagar: ", compraTotal)
            print("Desea realizar el pago? [1. Si / 2. No]: ", end="")
            respuesta = int(input())

            if respuesta == 1:
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
            else:
                metodoP = MetodoPago()
                metodoP.metodoPago(compraTotal)

        elif opcionPago == 3:
            print("::..............................................................................................::")
            print("::                                         TARJETA DE CRÉDITO                                   ::")
            print("::..............................................................................................::\n")
            print("Las tarjetas de crédito poseen un recargo del 25%\n")
            print("Importe Bruto: ", compraTotal)
            print("\nAplicando el recargo de 25 %")
            compraTotal += compraTotal * 0.25
            print("Importe neto a pagar: ", compraTotal)
            print("\n¿Desea realizar el pago? [1.Si / 2.No]: ", end="")
            respuesta = int(input())

            if respuesta == 1:
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
            else:
                metodoP = MetodoPago()
                metodoP.metodoPago(compraTotal)

        elif opcionPago == 4:
            print("::..............................................................................................::")
            print("::                                         MERCADO PAGO                                         ::")
            print("::..............................................................................................::\n")
            print("En pagos por Mercado Pago 5% de descuento")
            print("ALIAS: Interdata.mp")
            print("CBU: 00000238298729357")
            print("Importe bruto: ", compraTotal)
            print("\nAplicando el descuento")
            compraTotal -= compraTotal * 0.05
            print("Importe neto a pagar: ", compraTotal)
            print("¿Desea realizar el pago? [1.Si / 2.No]: ", end="")
            respuesta = int(input())

            if respuesta == 1:
                print("Su pago fue realizado con éxito")
                print("¡Gracias por su compra!\n")
            else:
                metodoP = MetodoPago()
                metodoP.metodoPago(compraTotal)

        elif opcionPago == 5:
            print("Volviendo a la sección productos")
            print("\nAguarde unos segundos...")
            llamada = Productos()
            llamada.productos()

        else:
            print("La opción ingresada no es válida")
            print("Por favor intentelo nuevamente")
