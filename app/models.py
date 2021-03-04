from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


engine = create_engine('mysql://lab:osmentos@mysqldb:3306/library', echo=True)

Base = declarative_base()


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    book_name = Column(String(64))
    author_name = Column(String(64))
    description = Column(String(300))
    # publish=DateField('Start Date', format='%m/%d/%Y')
    condition = Column(String(100))
    owner_id = Column(Integer)
    records = relationship("Record", back_populates="book")
    is_available = Column(Boolean,default=False)
    current_owner_id=Column(Integer)

Book.__table__.create(bind=engine, checkfirst=True)


class Record(Base):
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    _to = Column(Integer)
    _from = Column(Integer)
    book_id = Column(Integer, ForeignKey('books.id'))
    book = relationship("Book", back_populates="records")
    status =Column(String(20))


Record.__table__.create(bind=engine, checkfirst=True)
