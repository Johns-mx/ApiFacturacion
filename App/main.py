from fastapi import FastAPI, Request, status
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from Routes import cliente, empleado, factura, orden, platillo
from Config.methods import version
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import RequestValidationError


app = FastAPI(
    debug=True,
    title="ApiFacturacion",
    description="ApiFacturacion: api de un sistema de facturación para un restaurante.",
    version=version[1]
)


@app.on_event("startup")
async def startup():
    print("Application startup")

@app.on_event("shutdown")
async def shutdown():
    print("Application shutdown")


@app.get('/', tags=["Welcome"])
async def root():
    return {
        "error": False,
        "message": "ApiFacturacion: proyecto de administracion.",
        "res": None,
        "version": "0.0.1"
    }

#Funcion para responder cuando el usuario ingrese una ruta invalida
@app.exception_handler(StarletteHTTPException)
async def http_exception_handler(request: Request, exc: StarletteHTTPException):
    return JSONResponse(
        status_code=status.HTTP_404_NOT_FOUND,
        content=jsonable_encoder({
            "error": True,
            "message": "Ruta invalida.",
            "res": None,
            "version": version[1]
        })
    )

#Funcion para responder cuando faltan campos
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({
            "error": True,
            "message": "Inexistencia de campos.",
            "res": None,
            "version": version[1]
        })
    )

#Solucion CORS
origins= ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# >> despliega la api
if __name__=='__main__':
    uvicorn.run(app, host="0.0.0.0", port="8000")

# >> conexion de routers
app.include_router(cliente.cli)
app.include_router(empleado.emp)
app.include_router(factura.fac)
app.include_router(orden.ord)
app.include_router(platillo.prod)