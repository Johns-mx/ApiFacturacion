from fastapi import APIRouter, status
from Database.conexion import engine
from bs4 import BeautifulSoup
from sqlalchemy import text
from Models.index import platillo
from Config.methods import version, responseModelError2X, responseModelError4X
from Schemas.schemasRegistro import registroPlatillo
from Config.validations import verificarVacio
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


prod = APIRouter(prefix=f"/api/{version[0]}/platillo", tags=["Platillo"])


@prod.get('/')
async def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "error": False,
            "message": "API: Platillo",
            "res": None,
            "version": version[1]
        })
    )

# ********* ruta: REGISTRAR USUARIO *********


@prod.post('/registrar', status_code=200, response_model=registroPlatillo, tags=['Platillo'])
async def registrar(prod: registroPlatillo):

    # **** Obtenemos el correo introducido por el usuario y lo pasa por validador de Email
    nombrePlatillo = prod.nombrePlatillo.strip()
    nombrePlatillo = BeautifulSoup(nombrePlatillo, features='html.parser').text

    precioPlatillo = prod.precioPlatillo
    precioPlatillo = str(precioPlatillo).strip()
    precioPlatillo = BeautifulSoup(precioPlatillo, features='html.parser').text

    newPlatillo = {
        "nombrePlatillo": nombrePlatillo,
        "precioPlatillo": precioPlatillo
    }

    if newPlatillo:
        # *** Consultamos a la base de datos
        try:
            with engine.connect() as conn:
                conn.execute(platillo.insert().values(nombrePlatillo=nombrePlatillo, precioPlatillo=precioPlatillo))
        finally:
            conn.close()

        return responseModelError2X(status.HTTP_201_CREATED, False, "Platillo registrado correctamente.", None)
    else:
        return responseModelError4X(status.HTTP_400_BAD_REQUEST, True, "Existen campos vacios.", None)


