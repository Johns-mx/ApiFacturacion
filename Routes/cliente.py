from fastapi import APIRouter, status
import Database.conexion
from Models.index import cliente
from Config.methods import version
from Schemas.schemasRegistro import registroCliente
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


cli= APIRouter(prefix=f"/api/{version[0]}/cliente", tags=["Cliente"])


@cli.get('/')
async def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "error": False,
            "message": "API: Cliente",
            "res": None,
            "version": version[1]
        })
    )

# ********* ruta: REGISTRAR USUARIO *********
@cli.post('/registrar', status_code=200, response_model=registroCliente, tags=['Cliente'])
async def registrar(cli: registroCliente):
    pass