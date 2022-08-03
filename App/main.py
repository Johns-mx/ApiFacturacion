from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(debug=True,
    title="ApiFacturacion",
    description="ApiFacturacion: api de un sistema de facturación para un restaurante.",
    version="0.0.1")


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