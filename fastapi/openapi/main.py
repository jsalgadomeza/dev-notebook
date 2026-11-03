from fastapi import FastAPI
from schemas import Product

app = FastAPI()

@app.get("/")
def home():
    return {"mesage": "Hello, World!"}

@app.get("/products")
def get_products(limit: int = 5):
    return {
        "products": [
            "Product 1", "Product 2",
            "Product 3", "Product 4"
        ], 
        "limit": limit
    }

@app.get("/products/{product_id}")
def get_product(product_id: int, include_reviews: bool = False):
    return {"product_id": product_id, "include_reviews": include_reviews}

@app.post("/products", status_code=201)
def create_product(product: Product):
    return product