from fastapi import APIRouter, status
import Database.conexion
import Models.index
import Config.methods
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


prod= APIRouter(prefix="/producto", tags=["Producto"])

@prod.get('/')
async def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "error": False,
            "message": "API: Producto",
            "res": None,
            "version": "0.0.1"
        })
    )