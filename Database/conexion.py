import sqlalchemy as sa

URL = "mysql+pymysql://root:admin@localhost/sisfacturacion"

engine = sa.create_engine(URL,
    echo=False,
    pool_pre_ping=True,
    pool_timeout=20,
    pool_recycle=-1
)
meta = sa.MetaData()   #Para enviar propiedades a la tabla 'users'.
conn = engine.connect()   #Conectando engine a base de datos.