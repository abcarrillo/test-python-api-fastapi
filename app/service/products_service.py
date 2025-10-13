from app.repository.product_repository import ProductRepository
from sqlalchemy.orm import Session
from app.schema.product_schema import ProductResponse

class ProductService:
    @staticmethod
    def get_all_products(db: Session):
        resultList = ProductRepository.get_all_products(db)
        responseList = []
        for item in resultList:
            responseList.append(ProductResponse.model_validate(item, from_attributes=True))
        return responseList
    
    @staticmethod
    def get_product_by_id(id: int, db: Session):
        result = ProductRepository.get_product_by_id(id, db)
        return ProductResponse.model_validate(result, from_attributes= True)
    
    @staticmethod
    def create_product(product: ProductResponse, db: Session):
        return ProductRepository.create_product(product, db)