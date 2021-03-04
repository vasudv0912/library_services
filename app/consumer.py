from kafka import KafkaConsumer
from sqlalchemy.orm import sessionmaker
from multiprocessing import Process
import json
from models import Book, Record
import sqlalchemy

bootstrap_servers = ['172.17.0.1:9091']
engine = sqlalchemy.create_engine(
    'mysql://lab:osmentos@mysqldb:3306/library', echo=True)


def value_deserializer(m): return json.loads(m.decode('utf-8'))


Session = sessionmaker(bind=engine)
session = Session()

# topics=['add_book']


def add_book():
    try:
        consumer = KafkaConsumer(
            'add_book', bootstrap_servers=bootstrap_servers, value_deserializer=value_deserializer)
    except Exception as e:
        print(str(e))

    for message in consumer:
        print(message.value)
        ed = Book(book_name=message.value['book_name'], author_name=message.value['author_name'],
                  description=message.value['description'], condition=message.value['condition'], owner_id=message.value['owner_id'],is_available=True)
        session.add(ed)
        session.commit()


Process(target=add_book).start()


def issue_book():
    try:
        consumer = KafkaConsumer(
            'issue_book', bootstrap_servers=bootstrap_servers, value_deserializer=value_deserializer)

    except Exception as e:
        print(str(e))

    for message in consumer:
        print(message.value)
        book = session.query(Book).filter_by(
            id=message.value['book_id']).first()
        if is_available:
            ed = Record(_from = book.current_owner_id,_to = message.value['_to'],status ="pending")
            book.is_available=False
            book.records.append(ed)
            session.add(book)
            session.commit()


Process(target=issue_book).start()


def edit_book():
    try:
        consumer = KafkaConsumer(
            'edit_book', bootstrap_servers=bootstrap_servers, value_deserializer=value_deserializer)
    except Exception as e:
        print(str(e))

    for message in consumer:
        print(message.value)
        book = session.query(Book).filter_by(
            owner_id=message.value['owner_id']).first()
        book.book_name = message.value['book_name']
        book.author_name = message.value['author_name']
        book.description = message.value['description']
        book.condition = message.value['condition']
        session.commit()


Process(target=edit_book).start()





def release_book():
     try:
        consumer = KafkaConsumer(
            'release_book', bootstrap_servers=bootstrap_servers, value_deserializer=value_deserializer)
    except Exception as e:
        print(str(e))

    for message in consumer:
        print(message.value)
        book = session.query(Book).filter_by(
            id=message.value['book_id']).first()
        if book.current_owner_id==book.owner_id:
            book.is_available=True
            session.add(book)
            session.commit()

