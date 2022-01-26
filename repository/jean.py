from sqlalchemy.orm import Session
from sqlalchemy.sql import text
import models, schemas
from fastapi import HTTPException, status


# def get_all(db: Session):
#     return db.query(models.Jean).all()


def get_all(db: Session, current_user: schemas.User, pg: int):
    db.execute(f'''
                create table ex as select distinct(p.product_id), (p.ratew*pr.rating + p.tpw*pr.trend + pa.apw*pr.agegroup) as weight  from products p
                join products_age pa
                on pa.product_id= p.product_id
                join age a
                on pa.agegroup = a.agegroup
                join preference pr
                on pr.a_agegroup = a.agegroup and pr.userid={current_user.id}
                and rownum<=250 order by weight desc
            ''')
    r = db.execute(f'''
                select p.product_id, 
                p.name, p.hashtag, p.rating, p.image, p.xs_size, p.purchase_total,
                p.view_total, p.purchase_age, p.view_age, p.price, p.heart, avg(1- abs((r.height/r.weight)-(u.height/u.weight))) as np from uinfo u
                join preference pr
                on u.id=pr.userid
                join age a
                on u.agegroup=a.agegroup
                join products_age pa
                on pa.agegroup=u.agegroup
                join products p
                on pa.product_id=p.product_id
                join reviews r
                on pa.product_id=r.product_id and r.height-5<=u.height and u.height<=r.height+5  and r.weight-5<=u.weight and u.weight<=r.weight+5 and u.id={current_user.id}
                join ex e
                on p.product_id = e.product_id
                group by p.product_id, 
                p.name, p.hashtag, p.rating, p.image, p.xs_size, p.purchase_total,
                p.view_total, p.purchase_age, p.view_age, p.price, p.heart
            ''').fetchall()
    db.execute('''drop table ex''')
    # return len(list(r))

    return r[(pg-1)*10+1:pg*10+1]
    # return db.query(models.Product).all()[(pg-1)*10+1:pg*10+1]
    # return db.query(models.Product).all()


def show(id: int, db: Session):
    jean = db.query(models.Jean).filter(models.Jean.id == id).first()
    if not jean:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Jean with the id {id} is not available")
    return jean


def create(request: schemas.Jean, db: Session):
    new_jean = models.Jean(title=request.title, body=request.body, user_id=3)
    db.add(new_jean)
    db.commit()
    db.refresh(new_jean)
    return new_jean


def destroy(id: int, db: Session):
    jean = db.query(models.Jean).filter(models.Jean.id ==
                                        id)
    if not jean.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"jean with id {id} not found")
    jean.delete(synchronize_session=False)
    db.commit()
    return 'done'


def update(id: int, request: schemas.Jean, db: Session):
    jean = db.query(models.Jean).filter(models.Jean.id ==
                                        id)
    if not jean.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Jean with id {id} not found")
    jean.update(dict(request))
    db.commit()
    return 'updated'
