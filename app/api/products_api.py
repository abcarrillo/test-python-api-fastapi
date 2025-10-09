from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.controller.product_controller import ProductController

router = APIRouter()

@router.get("/", include_in_schema=True)
async def greet():
    return "Hola Mundo!"

@router.get("/products", include_in_schema=True)
async def get_all_products(db: Session = Depends(get_db)):
    return ProductController.get_all_products(db)