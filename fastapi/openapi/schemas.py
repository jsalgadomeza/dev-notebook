from pydantic import BaseModel, Field


class Product(BaseModel):
    id: int | None = None
    name: str = Field(min_length=1, max_length=10)
    description: str | None = None
    price: float = Field(gt=0)
    stock: int = Field(ge=0)
