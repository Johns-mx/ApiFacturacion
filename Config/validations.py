import re


#**** Comprobamos si los inputs estan vacios ****
def verificarVacio(x):
    for i in x.values():
        if len(i) == 0:
            return True
        else:
            return False

# VALIDANDO EMAIL: expresiones regulares
def es_correo_valido(correo):
    expresion_regular = r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$"
    return re.match(expresion_regular, correo) is not None


# VALIDANDO PHONE: expresiones regulares
def es_telefono_valido(phone):
    expresion_regular = r"^[+]?(\d{1,4})?\s?-?[.]?[(]?\d{3}[)]?\s?-?[.]?\d{3}\s?-?[.]?\d{4}$"
    return re.match(expresion_regular, phone) is not None


# VALIDANDO USERNAME: expresiones regulares
def es_usuario_valido(username):
    expresion_regular = r"^[a-zA-Z0-9@]+[._a-zA-Z0-9@]{5,34}$"
    return re.match(expresion_regular, username) is not None


# VALIDANDO PASSWORD: expresiones regulares
def es_password_valido(password):
    expresion_regular = r"^\S(.|\s){7,200}$"
    return re.match(expresion_regular, password) is not None


# VALIDANDO NAME: expresiones regulares
def es_nombre_valido(name):
    expresion_regular = r"^[a-zA-ZàáâäãåąčćęèéêëėįìíîïłńòóôöõøùúûüųūÿýżźñçčšžÀÁÂÄÃÅĄĆČĖĘÈÉÊËÌÍÎÏĮŁŃÒÓÔÖÕØÙÚÛÜŲŪŸÝŻŹÑßÇŒÆČŠŽ∂ð ]+$"
    return re.match(expresion_regular, name) is not None