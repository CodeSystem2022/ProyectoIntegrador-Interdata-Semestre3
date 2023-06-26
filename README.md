# Proyecto Integrador - Tercer semestre
# Conversión del proyecto desde Java a Python
![Logo Interdata Color-02](https://user-images.githubusercontent.com/112593194/236959451-08cbc3fb-cc4a-4650-aeaa-2996dbb91046.jpg)
### Integrantes:
:small_blue_diamond: Ignacio Buchter
:small_blue_diamond: Daiana Figueroa
:small_blue_diamond: Gabriel Echave 
:small_blue_diamond: Franco Bianchi 
:small_blue_diamond: Silvina Prado
:small_blue_diamond: Francisco Chahla 
# TIENDA DE ROPA MASCULINA
## Proyecto Integrador
Éste proyecto fue desarrollado con anterioridad en PseInt y Java para luego ser adaptado al lenguaje de Python. El mismo consiste en una tienda de ropa masculina que se dedica a la venta mayorista, se vende por curva de 5 unidades, talles y colores sin elección.

## Pasos 💻
### Paso 1 
Al ejecutar el programa nos dirige al InicioTienda. El cual nos ofrece 3 opciones:

1. Iniciar sesión con su cuenta;   # Se verificara si la cuenta se encuentra en la base de datos
2. Registrar nuevo usuario;        # Se Agregara un usuario y contraseña a la base de datos
3. Salir de la página;

Las dos primeras opciones nos lleva a la sección Productos mientras que la última finaliza la ejecución del programa.
### Paso 2
En la sección Productos podemos encontrar:

1. Remeras;
2. Buzos;
3. Camperas;
4. Jeans;
5. Pantalones Joggin;
6. Camisas;
7. Trajes;
8. Ver carrito de compras;
9. Salir de la cuenta;

Cada opción al seleccionarla despliega sus diferentes modelos para cada categoria, los cuales podemos ir agregando al carrito. Todas estas categorias funcionan con un mismo metodo que muestra al usuario una N cantidad de productos y le permite seleccionar el que desea. El metodo toma el nombre y precio de los productos de una base de datos, de esta forma no hace falta modificar el codigo para agregar nuevos items, sino solo agregarlos a la base de datos. 

### Paso 3
El programa nos pregunta si queremos añadir el producto al carrito. En el que caso de que si esta operacion se guarda en la base de datos para que luego el usuario pueda visualizar los productos que agrego tanto como su precio y cantidad.

..................................................................................................
::                                         CARRITO                                              ::
..................................................................................................

En carrito:
|--- Puma X2 = $2400
|--- Nike X1 = $1900 

Total de compra $: 4300

..................................................................................................

1.Ir a pagar
2.Volver atras

### Paso 4
Una vez que tenemos los productos que deseamos comprar añadidos al carrito de compras, podemos proceder al pago.
Para el pago la tienda ofrece diferentes métodos:

1. Transferencia bancaria;
2. Tarjeta de Débito;
3. Tarjeta de Crédito;
4. Mercado Pago;
5. Volver atrás;

### Paso 5
Dependiendo del método de pago elegido son los datos que nos solicitará al igual que el descuento o recargo que obtendremos, una vez que hemos terminado de comprar podemos salir para así finalizar la ejecución del programa, o seguir comprando. Al finalizar al compra se guarda en la base de datos el monto, el metodo de pago y la fecha y hora de la compra.
