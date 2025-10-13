from pydantic import BaseModel
class ProductResponse(BaseModel):
    id: int | None = None
    name: str
    description: str
    price: float
    quantity: int