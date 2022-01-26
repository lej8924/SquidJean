from sqlalchemy.orm import Session
import models, schemas
from fastapi import HTTPException, status


def get_all_review(db: Session, num: int):
    return db.query(models.Review).join(models.Product).filter(models.Review.product_id == num)[0:4]


def get_one_product(db: Session, num: int):
    return db.query(models.Product).filter(models.Product.product_id == num).first()


def null_num(db: Session, num: int):
    product_id = db.query(models.Product.product_id).filter(
        models.Product.product_id == num)
    if not product_id:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Jean with id {id} not found")
    return 'null_num'
