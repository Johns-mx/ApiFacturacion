from fastapi import APIRouter, status
import Database.conexion
from Models.index import platillo
from Config.methods import version
from Schemas.schemasRegistro import registroPlatillo
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


prod= APIRouter(prefix=f"/api/{version[0]}/platillo", tags=["Platillo"])

@prod.get('/')
async def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "error": False,
            "message": "API: Producto",
            "res": None,
            "version": version[1]
        })
    )

# ********* ruta: REGISTRAR USUARIO *********
@prod.post('/registrar', status_code=200, response_model=registroPlatillo, tags=['Platillo'])
async def registrar(prod: registroPlatillo):
    pass