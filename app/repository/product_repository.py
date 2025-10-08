from app.models import product_model
from fastapi import Depends
from sqlalchemy.orm import Session
from app.db.session import get_db

class ProductRepository:
    @staticmethod
    def get_all_products(db: Session = Depends(get_db)):
        db_products = db.query(product_model.Product).all()
        return db_products