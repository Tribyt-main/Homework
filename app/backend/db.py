from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import Column, Integer, String

engine = create_engine('sqlite:///ecomnerce.db', echo=True)

session_local = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
