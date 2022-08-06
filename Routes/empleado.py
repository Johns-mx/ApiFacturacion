from fastapi import APIRouter, status
from Database.conexion import engine
from Models.index import empleado
from Schemas.schemasRegistro import registroEmpleado, loginEmpleado
from Config.methods import version
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
            "version": "0.0.1"
        })
    )


# ********* ruta: REGISTRAR USUARIO *********
@emp.post('/registrar', status_code=200, response_model=registroEmpleado, tags=['Empleado'])
async def registrar(emp: registroEmpleado):

    # Obtenemos el correo introducido por el usuario y lo pasa por validador de Email
    username = emp.username.strip()
    username = BeautifulSoup(username, features='html.parser').text

    name = emp.name.strip()
    name = BeautifulSoup(name, features='html.parser').text

    password = emp.password.strip()
    password = BeautifulSoup(password, features='html.parser').text

    email = emp.email.strip()
    email = BeautifulSoup(email, features='html.parser').text

    position = emp.position.strip()
    position = BeautifulSoup(phone, features='html.parser').text

    # Creamos un diccionario con los valores del usuario
    newUser = {"username": username, "password": password,
               "email": email, "name": name, "phone": phone}

    if verificarVacio(newUser) == False:
        # Empezamos a procesar el name
        if es_nombre_valido(name) == True:
            # Empezamos a procesar el username
            if es_usuario_valido(username) == True:
                # Empezamos a procesar el correo electronico
                if es_correo_valido(email) == True:
                    # Empezamos a procesar el numero de telefono
                    if es_telefono_valido(phone) == True:

                        # Elimina los caracteres del phone
                        phone = re.sub("\!|\'|\?|\ |\(|\)|\-|\+", "", phone)

                        if es_password_valido(password) == True:
                            # Encodea el password
                            passw = password.encode()
                            passw = encrytPassw(passw)

                            try:
                                # Usamos el procedimiento almacenado para registrar el usuario y el token generado.
                                with engine.connect() as conn:
                                    cursor = conn.connection.cursor()
                                    arg = (username, passw,
                                           email, name, phone, 0)
                                    cursor.callproc('registerUser', args=arg)
                                    conn.connection.commit()
                                    output = cursor.fetchone()
                                    output = output[0]
                            finally:
                                conn.close()

                            if output == 1:

                                token = generarToken()
                                login = autoLogin(email, passw)

                                try:
                                    with engine.connect() as conn:
                                        conn.execute(keys.insert().values(
                                            keyUser=token, appConnect="default", userID=login))
                                finally:
                                    conn.close()

                                return responseModelError2X(status.HTTP_201_CREATED, False, "Usuario agregado correctamente.",
                                                            {"appConnect": "default", "keyUser": token})
                            else:
                                return responseModelError4X(status.HTTP_400_BAD_REQUEST, True, "El usuario que intenta registrar ya existe.", None)
                        else:
                            return responseModelError4X(status.HTTP_401_UNAUTHORIZED, True, "La contraseña no cumple con los requisitos.", None)
                    else:
                        return responseModelError4X(status.HTTP_401_UNAUTHORIZED, True, "Número de teléfono inválido.", None)
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
async def login(empleado: loginEmpleado):
    pass