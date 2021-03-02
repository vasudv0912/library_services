from kafka import KafkaConsumer
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import json

engine = sqlalchemy.create_engine('mysql://lab:osmentos@mysqldb:3306/sqlalchemy',echo=True)
session = sessionmaker(bind=engine)
session.configure(bind=engine)


Base = declarative_base()

class User(Base):
    __tablename__ = 'library'
    id = Column(Integer, primary_key=True)
    book_name = Column(String(64))
    author_name =Column(String(64))
    description= Column(String(300))
    # publish=DateField('Start Date', format='%m/%d/%Y')
    condition=Column(String(100))


    

consumer = KafkaConsumer('books', bootstrap_servers=['172.17.0.1:9091'] , value_deserializer=lambda m: json.loads(m.decode('utf-8')))
for message in consumer:
    print (message.value)
    ed=User(book_name=message.value['book_name'],author_name='VASU',description='HAPPY BIRTHDAY')
    session.add(ed)
