from sqlalchemy.orm import Session
from app.service.products_service import ProductService
from app.schema.product_schema import ProductResponse

class ProductController:
    @staticmethod
    def get_all_products(db: Session):
        return ProductService.get_all_products(db)
    
    @staticmethod
    def get_product_by_id(id: int, db: Session):
        return ProductService.get_product_by_id(id, db)
    
    @staticmethod
    def create_product(product: ProductResponse, db: Session):
        return ProductService.create_product(product, db)
    
    @staticmethod
    def update_product(id: int, product: ProductResponse, db: Session):
        return ProductService.update_product(id, product, db)
    
    @staticmethod
    def delete_product(id: int, product: ProductResponse, db: Session):
        return ProductService.delete_product(id, product, db)