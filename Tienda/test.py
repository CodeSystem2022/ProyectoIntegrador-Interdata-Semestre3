from Tienda import InicioTienda
from database import Conexion

if __name__ == '__main__':
    conexion = Conexion.obtenerConexion()
    tienda = InicioTienda(conexion)
    tienda.inicio_tienda()