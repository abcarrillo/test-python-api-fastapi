from app.models import product_model
from sqlalchemy.orm import Session
from app.schema.product_schema import ProductResponse

class ProductRepository:
    @staticmethod
    def get_all_products(db: Session):
        db_products = db.query(product_model.Product).all()
        return db_products
    
    @staticmethod
    def get_product_by_id(id: int, db: Session):
        db_product = db.query(product_model.Product).filter(product_model.Product.id == id).first()
        return db_product
    
    @staticmethod
    def create_product(product: ProductResponse, db: Session):
        """
        Crea un nuevo producto ignorando el ID que envie el cliente
        """
        new_product = product_model.Product(**product.model_dump())
        new_product.id = None
        # print(new_product.id, new_product.name, new_product.description, new_product.price, new_product.quantity)
        db.add(new_product)
        db.commit()
        return "OK"
    
    @staticmethod
    def update_product(id:int, product: ProductResponse, db: Session):
        db_product = db.query(product_model.Product).filter(product_model.Product.id == id).first()
        if db_product:
            db_product.name = product.name
            db_product.description = product.description
            db_product.price = product.price
            db_product.quantity = product.quantity
            db.commit()
            return db_product
        return None