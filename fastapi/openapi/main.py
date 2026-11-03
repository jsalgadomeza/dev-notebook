from fastapi import FastAPI, HTTPException
from routers.products import router as products_router
from schemas import Product

app = FastAPI()
app.include_router(products_router)

@app.get("/")
def home():
    return {"mesage": "Hello, World!"}
