from fastapi import APIRouter, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder

from service.products import ProductsService
from schemas.products import Product
from config.database import Session 


product_router = APIRouter()

@product_router.post('/product/',tags=['product'], status_code=201)
def create_product(product:Product):
    db = Session()
    ProductsService(db).create_product(product)
    return JSONResponse(content={"message":"product created successfully",'status_code':201})

@product_router.get('/product/', tags = ['product'], status_code=200)
def get_product():
    db = Session()
    result = ProductsService(db).get_product()
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@product_router.get('/product_for_id/', tags=['product'],status_code=200)
def get_product_for_id(id:int):
    db = Session()
    result = ProductsService(db).get_for_id(id)
    return JSONResponse(content=jsonable_encoder(result), status_code= 200)

@product_router.put('/product{id}/',tags=['product'])
def update_product(id:int,data:Product):
    db = Session()
    result = ProductsService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"product don't found","status_code":404})
    ProductsService(db).update_product(data)
    return JSONResponse(content={"message":"product update successfully",'status_code':202}, status_code=200)


@product_router.delete('/product{id}/', tags=['product'])
def delete_product(id:int):
    db = Session()
    result = ProductsService(db).get_for_id(id)
    if not result:
        return JSONResponse(content={"message":"product don't found","status_code":404})
    ProductsService(db).delete_product(id)
    return JSONResponse(content={"message":"product delete successfully",'status_code':200}, status_code=200)