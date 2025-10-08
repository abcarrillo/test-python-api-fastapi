from sqlalchemy.orm import Session
from app.service.products_service import ProductService

class ProductController:
    @staticmethod
    def get_all_products(db: Session):
        return ProductService.get_all_products(db)