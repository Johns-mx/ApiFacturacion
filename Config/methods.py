import bcrypt, base64, hashlib
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

#Metodos de control de versiones
def APIversion():
    verApi= ("v1", "v1.1.0")
    return verApi

version= APIversion()


#Metodo para enviar respuesta 200 ~
def responseModelError2X(status_code, error: bool, message, res):
    return JSONResponse(
        status_code= status_code,
        content=jsonable_encoder({
            "error": error,
            "message": message,
            "res": res,
            "version": version[1]
        }),
    )

#Metodo para enviar respuesta 400 ~
def responseModelError4X(status_code, error: bool, message, res):
    return JSONResponse(
        status_code= status_code,
        content=jsonable_encoder({
            "error": error,
            "message": message,
            "res": res,
            "version": version[1]
        }),
    )

#**** FUNCION PARA ENCRIPTAR EL PASSWORD DE USUARIO ****
def encrytPassw(passw):

    with open('./config/secretKey.txt') as file:
        secretKey = file.read()
        secretKey = bytes(secretKey, encoding='ascii')
        file.close()

    key = bcrypt.kdf(
        password=passw,
        salt=secretKey,
        desired_key_bytes=64,
        rounds=100
    )

    passwd = base64.b64encode(hashlib.sha256(key).digest())
    return passwd