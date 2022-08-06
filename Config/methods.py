from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

#Metodos de control de versiones
def APIversion():
    verApi= ("v1", "v1.4.0")
    return verApi

version= APIversion()