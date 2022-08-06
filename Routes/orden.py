from fastapi import APIRouter, status
import Database.conexion
from Models.index import orden
from Config.methods import version
from Schemas.schemasRegistro import registroOrden
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


ord= APIRouter(prefix=f"/api/{version[0]}/orden", tags=["Orden"])

@ord.get('/')
async def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "error": False,
            "message": "API: Orden",
            "res": None,
            "version": "0.0.1"
        })
    )

# ********* ruta: REGISTRAR USUARIO *********
@ord.post('/registrar', status_code=200, response_model=registroOrden, tags=['Orden'])
async def registrar(ord: registroOrden):
    pass