from fastapi import APIRouter, status
import Database.conexion
from Models.index import factura
from Config.methods import version
from Schemas.schemasRegistro import registroFactura
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


fac= APIRouter(prefix=f"/api/{version[0]}/factura", tags=["Factura"])

@fac.get('/')
async def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "error": False,
            "message": "API: Factura",
            "res": None,
            "version": "0.0.1"
        })
    )

# ********* ruta: REGISTRAR USUARIO *********
@fac.post('/registrar', status_code=200, response_model=registroFactura, tags=['Factura'])
async def registrar(fac: registroFactura):
    pass