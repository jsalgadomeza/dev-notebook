from fastapi import FastAPI
from routers.products import router as products_router
from routers.llm import router as llm_router

app = FastAPI()
app.include_router(products_router)
app.include_router(llm_router)

@app.get("/")
def home():
    return {"mesage": "Hello, World!"}
