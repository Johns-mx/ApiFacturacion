from fastapi import APIRouter, status
from Database.conexion import engine
from bs4 import BeautifulSoup
from Models.index import empleado
from Schemas.schemasRegistro import registroEmpleado, loginEmpleado
from Config.methods import version, encrytPassw, responseModelError2X, responseModelError4X
from Config.validations import es_correo_valido, es_nombre_valido, es_password_valido, es_usuario_valido, verificarVacio
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


emp= APIRouter(prefix=f"/api/{version[0]}/empleado", tags=["Empleado"])


@emp.get('/')
async def root():
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=jsonable_encoder({
            "error": False,
            "message": "API: Empleado",
            "res": None,
            "version": version[1]
        })
    )


# ********* ruta: REGISTRAR USUARIO *********
@emp.post('/registrar', status_code=200, response_model=registroEmpleado, tags=['Empleado'])
async def registrar(emp: registroEmpleado):

    # Obtenemos el correo introducido por el usuario y lo pasa por validador de Email
    username = emp.username.strip()
    username = BeautifulSoup(username, features='html.parser').text

    email = emp.email.strip()
    email = BeautifulSoup(email, features='html.parser').text
    
    password = emp.password.strip()
    password = BeautifulSoup(password, features='html.parser').text
    
    name = emp.name.strip()
    name = BeautifulSoup(name, features='html.parser').text

    position = emp.position.strip()
    position = BeautifulSoup(position, features='html.parser').text

    # Creamos un diccionario con los valores del usuario
    newUser = {
        "username": username, "email": email,
        "password": password, "name": name,
        "position": position
    }

    if verificarVacio(newUser) == False:
        # Empezamos a procesar el name
        if es_nombre_valido(name) == True:
            # Empezamos a procesar el username
            if es_usuario_valido(username) == True:
                # Empezamos a procesar el correo electronico
                if es_correo_valido(email) == True:
                    # Empezamos a procesar el numero de telefono
                    if es_password_valido(password) == True:
                        
                        # Encodea el password
                        passw = password.encode()
                        passw = encrytPassw(passw)
                            
                        try:
                            # Usamos el procedimiento almacenado para registrar el empleado.
                            with engine.connect() as conn:
                                cursor = conn.connection.cursor()
                                arg = (username, email, passw, name, position, 0)
                                cursor.callproc('registerEmpleado', args=arg)
                                conn.connection.commit()
                                output = cursor.fetchone()
                                output = output[0]
                            
                            if output == 1:
                                return responseModelError2X(status.HTTP_201_CREATED, False, "Usuario agregado correctamente.", None)
                            else:
                                return responseModelError4X(status.HTTP_400_BAD_REQUEST, True, "El usuario que intenta registrar ya existe.", None)
                        finally:
                            conn.close()
                    else:
                        return responseModelError4X(status.HTTP_401_UNAUTHORIZED, True, "La contraseña no cumple con los requisitos.", None)
                else:
                    return responseModelError4X(status.HTTP_401_UNAUTHORIZED, True, "Correo electrónico inválido.", None)
            else:
                return responseModelError4X(status.HTTP_401_UNAUTHORIZED, True, "Nombre de usuario inválido.", None)
        else:
            return responseModelError4X(status.HTTP_401_UNAUTHORIZED, True, "El nombre no cumple con los requisitos.", None)
    else:
        return responseModelError4X(status.HTTP_400_BAD_REQUEST, True, "Existen campos vacios.", None)


# ********* ruta: REGISTRAR USUARIO *********
@emp.post('/login', status_code=200, response_model=loginEmpleado, tags=['Empleado'])
async def login(emp: loginEmpleado):
    
    # CAMPO: uceCampo: username, telefono, email
    email = emp.email.strip()
    email = BeautifulSoup(email, features='html.parser').text
    
    password = emp.password.strip()
    password = BeautifulSoup(password, features='html.parser').text
    passw = password.encode()
    passw = encrytPassw(passw)
    
    dataLogin = {"email": email, "password": passw}

    # Comprueba los campos y ejecuta las conexiones
    if verificarVacio(dataLogin) == False:

        if es_correo_valido(email) == True:

            try:
                # Usando procedimiento almacenado: loginEmail
                with engine.connect() as conn:
                    cursor = conn.connection.cursor()
                    arg = (email, passw,)
                    cursor.callproc('loginEmail', args=arg)
                    conn.connection.commit()
                    output = cursor.fetchone()
            finally:
                conn.close()

            if output != None:
                # Almacenamos el userID del usuario en 'userIDK'
                output = output[0]
                return responseModelError2X(status.HTTP_200_OK, False, "Inicio de seccion correctamente.", None)
            else:
                return responseModelError4X(status.HTTP_404_NOT_FOUND, False, "Usuario no encontrado", None)
        else:
            return responseModelError4X(status.HTTP_401_UNAUTHORIZED, True, "Correo electronico invalido.", None)
    else:
        return responseModelError4X(status.HTTP_400_BAD_REQUEST, True, "Existen campos vacios.", None)