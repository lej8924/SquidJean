from fastapi import APIRouter, Depends, Request
import schemas, database, view
from sqlalchemy.orm import Session
from repository import user
from fastapi.responses import HTMLResponse


router = APIRouter(
    prefix='/user',
    tags=['users']
)
get_db = database.get_db


@router.get('/', response_class=HTMLResponse)
async def login(request: Request):
    return view.signup(request)


@router.post('/', response_model=schemas.ShowUser)
async def create_user(height: str = '', request: schemas.User = Depends(schemas.User.as_form), db: Session = Depends(get_db)):
    return user.create(request, height, db)


@router.get('/{id}', response_model=schemas.ShowUser)
async def get_user(id: int, db: Session = Depends(get_db)):
    return user.show(id, db)
