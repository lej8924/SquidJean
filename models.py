from sqlalchemy.sql.expression import null
from sqlalchemy.sql.schema import ForeignKey
from database import Base
from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy import Sequence
from sqlalchemy.orm import relationship
from sqlalchemy.dialects import oracle


class User(Base):
    __tablename__ = 'uinfo'

    id_seq = Sequence('USER_ID_SEQ', metadata=Base.metadata, minvalue=1001000)
    id = Column(Integer, Sequence('USER_ID_SEQ'), primary_key=True)
    username = Column(String(100), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False, unique=True)
    phonenumber = Column(String(100), nullable=False, unique=True)
    birthday = Column(String(100))
    agegroup = Column(Integer, ForeignKey('age.agegroup'))
    height = Column(Integer)
    weight = Column(Integer)
    jeansize = Column(String(10))


class Preference(Base):
    __tablename__ = 'preference'

    userid = Column(Integer, ForeignKey('uinfo.id'), primary_key=True)
    a_agegroup = Column(Integer, ForeignKey('age.agegroup'), primary_key=True)
    trend = Column(Float)
    agegroup = Column(Float)
    rating = Column(Float)


class Style(Base):
    __tablename__ = "style"

    userid = Column(Integer, ForeignKey('uinfo.id'), primary_key=True)
    wide = Column(Float)
    slim = Column(Float)
    tapered = Column(Float)
    crop = Column(Float)


class Product(Base):
    __tablename__ = 'products'

    product_id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    hashtag = Column(String(200))
    rating = Column(Float)
    image = Column(String(200))
    xs_size = Column(String(10))
    purchase_total = Column(String(100))
    view_total = Column(String(100))
    purchase_age = Column(String(100))
    view_age = Column(String(100))
    price = Column(Integer)
    heart = Column(Integer)
    ratew = Column(Float)
    tpw = Column(Float)


class Review(Base):
    __tablename__ = 'reviews'

    review_id = Column(Integer,  primary_key=True)
    product_id = Column(Integer, ForeignKey('products.product_id'))
    name = Column(String(100), nullable=False)
    gender = Column(String(10))
    height = Column(Integer)
    weight = Column(Integer)
    rating = Column(Float)
    fit_size = Column(String(4))
    evls = Column(Integer)
    evlb = Column(Integer)
    evlc = Column(Integer)
    evlt = Column(Integer)
    link = Column(String(1000))


class Age(Base):
    __tablename__ = "age"

    agegroup = Column(Integer,  primary_key=True)


class ProductAge(Base):
    __tablename__ = "products_age"

    product_id = Column(Integer, ForeignKey(
        'products.product_id'), primary_key=True)
    agegroup = Column(Integer, ForeignKey('age.agegroup'), primary_key=True)
    apw = Column(Float)
