# inicio tienda

from productos.tienda import *
from menus.tienda import *
class InicioTienda:
    def __init__(self):
        self.eleccionInicio = 0
        self.usuario = ""
        self.usuario1 = ""
        self.clave = ""
        self.clave1 = ""
        self.clave2 = ""
        self.opcion = 0
        self.salir = False

    def isSalir(self):
        return self.salir

    def setSalir(self, salir):
        self.salir = salir

    def getEleccionInicio(self):
        return self.eleccionInicio

    def setEleccionInicio(self, eleccionInicio):
        self.eleccionInicio = eleccionInicio

    def getUsuario(self):
        return self.usuario

    def setUsuario(self, usuario):
        self.usuario = usuario

    def getUsuario1(self):
        return self.usuario1

    def setUsuario1(self, usuario1):
        self.usuario1 = usuario1

    def getClave(self):
        return self.clave

    def setClave(self, clave):
        self.clave = clave

    def getClave1(self):
        return self.clave1

    def setClave1(self, clave1):
        self.clave1 = clave1

    def getClave2(self):
        return self.clave2

    def setClave2(self, clave2):
        self.clave2 = clave2

    def getOpcion(self):
        return self.opcion

    def setOpcion(self, opcion):
        self.opcion = opcion

    def inicioTienda(self):
        self.setClave(self.clave)
        self.setClave1(self.clave1)
        self.setEleccionInicio(self.eleccionInicio)
        self.setOpcion(self.opcion)
        self.setUsuario(self.usuario)
        self.setUsuario1(self.usuario1)
        salir = True
        self.setSalir(salir)

        llamada = Productos()

        while self.opcion != 3:
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
            print(" 1. Iniciar sesión con su cuenta")
            print(" 2. Registrar nuevo usuario")
            print(" 3. Salir de la página")
            print(" ")
            opcion = int(input("Ingrese una opción: "))

            usuario = "usuario123"
            clave = "1234"

            if opcion == 1:
                print(
                    ".........................................................................................................")
                print(
                    "::                                            MI CUENTA                                                ::")
                print(
                    "::.....................................................................................................::")
                usuario1 = input("\nUSUARIO: ")
                clave1 = input("CONTRASEÑA: ")

                if usuario == usuario1 and clave == clave1:
                    print("Redireccionando ....")
                    llamada.productos()
                else:
                    print("Los datos ingresados son incorrectos")
                    print("\nPor favor inténtelo nuevamente")
                    self.inicioTienda()

            elif opcion == 2:
                print(
                    ".........................................................................................................")
                print(
                    "::                                 CREANDO USUARIO EN TIENDA INTERDATA                                 ::")
                print(
                    "::.....................................................................................................::")
                print("\nIngrese los datos requeridos")
                usuario1 = input("\nNombre de usuario: ")
                clave1 = input("Contraseña: ")
                clave2 = input("Repita la contraseña: ")

                if clave1 == clave2:
                    print("")
                    print("¡Su cuenta fue creada con éxito!")
                    print("")
                    print("Redireccionando...")
                    llamada.productos()
                else:
                    print("\nLas contraseñas ingresadas no coinciden")
                    print("Por favor inténtelo nuevamente")
                    self.inicioTienda()

            elif opcion == 3:
                print("Saliendo de la página...")
                print("¡Gracias por visitarnos!")
                break

            else:
                print("La opción ingresada es incorrecta")
                print("\nPor favor inténtelo nuevamente..")
