from enum import Enum
from pydantic import BaseModel, Field
from typing import *


#class PositionType(str, Enum):
#Empleado = "Empleado"
#Administrador = "Administrador"

#***** REGISTRO ***** modelo
class registroEmpleado(BaseModel):
    username: str= Field(min_length=6, max_length=35)
    password: str= Field(min_length=8, max_length=201)
    name: str= Field(min_length=3, max_length=65)
    email: str= Field(max_length=65)
    position: str= Field(max_length=35)
    #position: PositionType

#***** REGISTRO ***** modelo
class registroCliente(BaseModel):
    nombreCliente: str= Field(max_length=35)
    apellidoCliente: str= Field(max_length=40)
    
#***** REGISTRO ***** modelo
class registroFactura(BaseModel):
    precioTotal: int
    metodoPago: str= Field(max_length=20)
    IdEmpleado: int
    IdOrden: int
    IdCliente: int

#***** REGISTRO ***** modelo
class registroOrden(BaseModel):
    IdPlatillo: int
    cantidad: int
    numeroMesa: int

#***** REGISTRO ***** modelo
class registroPlatillo(BaseModel):
    nombrePlatillo: str= Field(max_length=100)
    precioPlatillo: int


#***** LOGIN ****** modelo
class loginEmpleado(BaseModel):
    email: str
    password: str