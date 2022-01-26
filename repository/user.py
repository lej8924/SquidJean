from sqlalchemy.orm import Session
import models, schemas, hashing
from fastapi import HTTPException, status
from fastapi.responses import RedirectResponse
import datetime


def get_agegroup(birthday):
    date = datetime.date.today()
    year = int(date.strftime("%Y"))
    birthyear = int(str(birthday)[:4])
    agegroup = 0

    if 0 < year - birthyear < 19:
        agegroup = 1

    elif 19 <= year - birthyear < 24:
        agegroup = 2
    
    elif 24 <= year - birthyear < 29:
        agegroup = 3
    
    elif 29 <= year - birthyear <34:
        ageroup = 4
    
    elif 34 <= year - birthyear < 39:
        agegroup = 5
    
    else:
        agegroup = 6
    
    return agegroup


def create(request: schemas.User, passwordcheck: str, db: Session):

    user = dict(request)
    if user['password'] != passwordcheck:
        return 'password not correct'
    user.update(password=hashing.Hash.bcrypt(user['password']))
    user.update(agegroup=get_agegroup(user['birthday']))
    
    new_user = models.User(**user)  
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return RedirectResponse(
        '/auth', status_code=status.HTTP_302_FOUND)


def show(id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with the id {id} is not available")

    return user
