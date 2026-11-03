from fastapi import APIRouter, HTTPException
from schemas import Product
import storage

router = APIRouter(
    prefix = "/products",
    tags = ["products"]
)

@router.get("/")
def get_products(limit: int = 5):
    return list(storage.products.values())[:limit]

@router.get("/{product_id}")
def get_product(product_id: int):
    return storage.products.get(product_id)

@router.post("/", status_code=201)
def create_product(product: Product):
    product.id = storage.next_product_id
    storage.next_product_id += 1
    storage.products[product.id] = product
    return product

@router.delete("/{product_id}")
def delete_product(product_id: int):
    product = storage.products.pop(product_id, None)
    if product is None:
        raise HTTPException(
            status_code = 404,
            detail = f"Product with id {product_id} not found"
        )
    return {"message": f"Product with id {product_id} deleted successfully"}
