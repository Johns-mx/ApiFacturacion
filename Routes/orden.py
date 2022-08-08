from fastapi import APIRouter, status
from Database.conexion import engine
from bs4 import BeautifulSoup
from Models.index import orden
from Config.methods import version, responseModelError2X, responseModelError4X
from Schemas.schemasRegistro import registroOrden
from Config.validations import es_correo_valido, es_nombre_valido, es_password_valido, es_usuario_valido, verificarVacio
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


ord = APIRouter(prefix=f"/api/{version[0]}/orden", tags=["Orden"])


@ord.get('/')
async def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "error": False,
            "message": "API: Orden",
            "res": None,
            "version": version[1]
        })
    )


# ********* ruta: REGISTRAR ORDEN *********
@ord.post('/registrar', status_code=200, response_model=registroOrden, tags=['Orden'])
async def registrar(ord: registroOrden):

    # **** Obtenemos el correo introducido por el usuario y lo pasa por validador de Email
    name = ord.nombre.strip()
    name = BeautifulSoup(name, features='html.parser').text

    cantidad = ord.cantidad
    cant = str(cantidad).strip()
    cant = BeautifulSoup(cant, features='html.parser').text
    cantidad = int(cant)

    numeroMesa = ord.numeroMesa
    nMesa = str(numeroMesa).strip()
    nMesa = BeautifulSoup(nMesa, features='html.parser').text
    numeroMesa = int(nMesa)

    newOrden = {
        "nombre": name,
        "cantidad": cantidad,
        "numeroMesa": numeroMesa
    }

    if verificarVacio(newOrden) == True:
        if es_nombre_valido(name) == True:

            #*** Consultamos a la base de datos
            try:
                with engine.connect() as conn:
                    conn.execute(orden.insert().values(nombre=name, cantidad=cantidad, numeroMesa=numeroMesa))
            finally:
                conn.close()

            return responseModelError2X(status.HTTP_201_CREATED, False, "Orden realizada correctamente.", None)
        else:
            return responseModelError4X(status.HTTP_401_UNAUTHORIZED, True, "El nombre no cumple con los requisitos.", None)
    else:
        return responseModelError4X(status.HTTP_400_BAD_REQUEST, True, "Existen campos vacios.", None)