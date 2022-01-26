from ctypes import WinError
from pydantic import BaseModel
from typing import List, Optional
from fastapi import Form


class JeanBase(BaseModel):
    title: str
    body: str


class Jean(JeanBase):
    class Config():
        orm_mode = True


class User(BaseModel):
    username: str
    email: str
    password: str
    phonenumber: str
    birthday: str
    height: int
    weight: int
    jeansize: str

    @classmethod
    def as_form(
        cls,
        username: str = Form(...),
        email: str = Form(...),
        password: str = Form(...),
        phonenumber: str = Form(...),
        birthday: str = Form(...),
        height: str = Form(...),
        weight: str = Form(...),
        jeansize: str = Form(...)
    ):
        return cls(username=username, email=email, password=password, phonenumber=phonenumber, birthday=birthday, height=int(height), weight=int(weight), jeansize=jeansize)


class ShowUser(BaseModel):
    username: str
    email: str
    jeans: List[Jean] = []

    class Config():
        orm_mode = True


# class ShowJean(Jean):
#     buyer: ShowUser

#     class Config():
#         orm_mode = True

class ShowProduct(BaseModel):
    product_id: int
    name: str
    brand: str
    hashtag: Optional[str] = None
    rating: Optional[float] = None
    image: str
    xs_size: str
    purchase_total: str
    view_total: str
    purchase_age: str
    view_age: str
    price: int
    heart: int

    class Config():
        orm_mode = True

class ShowReview(BaseModel):
    review_id = int
    product_id = int
    name = str
    gender = str
    height = int
    weight = int
    rating = float
    fit_size = str
    evls = int
    evlb = int
    evlc = int
    evlt = int
    link = str
    
    class Config():
        orm_mode = True


class Login(BaseModel):
    email: str
    password: str

    @classmethod
    def as_form(
        cls,
        email: str = Form(...),
        password: str = Form(...)
    ):
        return cls(email=email, password=password)


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id: Optional[int] = None
    email: Optional[str] = None


class Preference(BaseModel):
    trend: int
    agegroup: int
    rating: int

    @classmethod
    def as_form(
        cls,
        trend: str = Form(...),
        agegroup: str = Form(...),
        rating: str = Form(...)
    ):
        return cls(trend=(4-int(trend)), agegroup=(4-int(agegroup)), rating=(4-int(rating)))


class Style(BaseModel):
    wide: float
    slim: float
    tapered: float
    crop: float

    @classmethod
    def as_form(
        cls,
        wide: str = Form(...),
        slim: str = Form(...),
        tapered: str = Form(...),
        crop: str = Form(...)
    ):
        return cls(wide=float(wide), slim=float(slim), tapered=float(tapered), crop=float(crop))
