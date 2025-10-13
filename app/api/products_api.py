from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.controller.product_controller import ProductController
from app.schema.product_schema import ProductResponse

router = APIRouter()

@router.get("/", include_in_schema=True)
async def greet():
    return "Hola Mundo!"

@router.get("/products", include_in_schema=True)
async def get_all_products(db: Session = Depends(get_db)):
    return ProductController.get_all_products(db)

@router.get("/products/{id}")
async def get_product_by_id(id: int, db: Session = Depends(get_db)):
    return ProductController.get_product_by_id(id, db)

@router.post("/products")
async def create_product(product: ProductResponse, db: Session = Depends(get_db)):
    return ProductController.create_product(product, db)