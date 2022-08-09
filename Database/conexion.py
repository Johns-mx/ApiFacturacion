import sqlalchemy as sa

URL = "mysql+pymysql://b780e3f9a3b014:24793b1e@us-cdbr-east-06.cleardb.net/heroku_83f7c8fd075dc39"

engine = sa.create_engine(URL,
    echo=False,
    pool_pre_ping=True,
    pool_timeout=20,
    pool_recycle=-1
)
meta = sa.MetaData()   #Para enviar propiedades a la tabla 'users'.
conn = engine.connect()   #Conectando engine a base de datos.