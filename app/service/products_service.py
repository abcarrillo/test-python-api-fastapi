from app.repository.product_repository import ProductRepository
from sqlalchemy.orm import Session

class ProductService:
    @staticmethod
    def get_all_products(db: Session):
        return ProductRepository.get_all_products(db)