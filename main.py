from fastapi import FastAPI
from fastapi.responses import HTMLResponse


from config.database import engine, Base

from middlewares.error_handler import Errorhandler
from routers.products import product_router
from routers.Supplier import supplier_router
from routers.Supplies import supplies_router


app = FastAPI()
app.title = "Mi app con FastAPI"
app.version = "0.0.1"

app.add_middleware(Errorhandler)
app.include_router(product_router)
app.include_router(supplier_router)
app.include_router(supplies_router)


Base.metadata.create_all(bind=engine)


@app.get("/", tags=["home"], status_code=200)
def message():
    return HTMLResponse("<h1>Hello World</h1>")


@app.get("/hola", tags=["home"])
def hola():
    return HTMLResponse("<h1>Hola Clase</h1>")
