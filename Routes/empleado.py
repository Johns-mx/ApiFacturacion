from fastapi import APIRouter, status
import Database.conexion
import Models.index
import Config.methods
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


emp= APIRouter(prefix="/empleado", tags=["Empleado"])

@emp.get('/')
async def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "error": False,
            "message": "API: Empleado",
            "res": None,
            "version": "0.0.1"
        })
    )