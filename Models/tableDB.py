"""
**** TABLAS PARA CREAR ****
- empleado(IdEmpleado, username, password, name, email, position, lastName)
    
- Cliente(Id_Cliente,Nombre_Cliente,Apellido_Cliente)
    
- Platillo(Id_Platillo,Nombre_Platillo,Precio_Platillo)

- Orden(Id_Orden,Cantidad,NumeroMesa,Id_Platillo)

- Factura(Id_Factura,FechaHora,PrecioTotal,MetodoPago,Id_Empleado,Id_Orden,Id_Cliente)
"""

from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, DECIMAL
from Database.conexion import meta, engine


empleado = Table(
    'empleado', meta,
    Column('IdEmpleado', Integer, primary_key=True, unique=True, autoincrement=True),
    Column('username', String(35), nullable=False, unique=True),
    Column('password', String(250), nullable=False, unique=True),
    Column('name', String(65), nullable=False),
    Column('email', String(65), nullable=False, unique=True),
    Column('position', String(26), nullable=False),
    Column('fechaRegistro', TIMESTAMP, nullable=True)
)

cliente = Table(
    'cliente', meta,
    Column('IdCliente', Integer, primary_key=True, unique=True, autoincrement=True),
    Column('nombreCliente', String(35), nullable=False),
    Column('apellidoCliente', String(40), nullable=False),
    Column('fechaCliente', TIMESTAMP, nullable=True)
)

platillo = Table(
    'platillo', meta,
    Column('IdPlatillo', Integer, primary_key=True, unique=True, autoincrement=True),
    Column('nombrePlatillo', String(100), nullable=False),
    Column('precioPlatillo', DECIMAL(10,2), nullable=False),
    Column('fechaPlatillo', TIMESTAMP, nullable=True)
)

orden = Table(
    'orden', meta,
    Column('IdOrden', Integer, primary_key=True, unique=True, autoincrement=True),
    Column('IdPlatillo', Integer, nullable=False),
    Column('nombre', String(100), nullable=False),
    Column('cantidad', Integer, nullable=False),
    Column('numeroMesa', Integer, nullable=False),
    Column('fechaOrden', TIMESTAMP, nullable=True)
)

factura = Table(
    'factura', meta,
    Column('IdFactura', Integer, primary_key=True, unique=True, autoincrement=True),
    Column('fechaFactura', TIMESTAMP, nullable=True),
    Column('precioTotal', DECIMAL(10,2), nullable=False),
    Column('metodoPago', String(20), nullable=False),
    Column('IdEmpleado', Integer, nullable=False),
    Column('IdOrden', Integer, nullable=False),
    Column('IdCliente', Integer, nullable=False)
)

meta.create_all(engine)     #Creando todo, las tablas, funciones, etc