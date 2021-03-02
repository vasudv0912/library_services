from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String



engine = create_engine('mysql://lab:osmentos@mysqldb:3306/library',echo=True)

Base = declarative_base()

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    book_name = Column(String(64))
    author_name =Column(String(64))
    description= Column(String(300))
    # publish=DateField('Start Date', format='%m/%d/%Y')
    condition=Column(String(100))


Book.__table__.create(bind=engine, checkfirst=True)