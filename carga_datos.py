from db.conexion import Conexion
from clases import persona, producto, detalle, factura

conexion = Conexion('supermark.db')
conexion.crear_db()

# Prueba carga de datos de persona aleatorio
listaPersonas = [("Mayra", "Velasquez", 36000123, "cliente"),
("Lionel", "Messi", 36811277, "administrador"),
("Edgar", "Hurtado", 32453897, "cliente"),
("Francisco", "Rosado", 23423533, "cliente")]

for i in listaPersonas:
    per = persona.Persona()
    per.crear_persona(i[0],i[1],i[2],i[3])

# Prueba de carga de datos de Productos
listaProductos = [("Harina 000", "Pampa Blanca", 30, 150),
("Harina 0000", "Pampa Blanca", 20, 160),
("Arroz", "Gallo de oro", 50, 130),
("Arroz", "10 Minutos", 45, 130),
("Fideos", "Luchetti", 70, 145.5),
("Fideos", "Marolio", 55, 130),
("Leche", "Sancor", 25, 250),
("Leche", "Cosalta", 25, 230)]


for j in listaProductos:
    pro = producto.Producto()
    pro.crear_producto(j[0], j[1], j[2], j[3])