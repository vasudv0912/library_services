from kafka import KafkaConsumer
from sqlalchemy.orm import sessionmaker
from multiprocessing import Process
import json
from models import Book
import sqlalchemy

bootstrap_servers=['172.17.0.1:9091'] 
engine = sqlalchemy.create_engine('mysql://lab:osmentos@mysqldb:3306/library',echo=True)
value_deserializer=lambda m: json.loads(m.decode('utf-8')) 
Session = sessionmaker(bind=engine)
session = Session()

# topics=['add_book']
def add_book():
    try:
        consumer = KafkaConsumer('add_book', bootstrap_servers=bootstrap_servers, value_deserializer=value_deserializer)
    except Exception as e:
        print(str(e))

    for message in consumer:
        print (message.value)
        ed=Book(book_name=message.value['book_name'],author_name='VASU',description='HAPPY BIRTHDAY')
        session.add(ed)
        session.commit()

# for topic in topics:
Process(target=add_book).start()
#     t.start()

# def issue_book():
#     try:
#         consumer = KafkaConsumer('issue_book', bootstrap_servers=bootstrap_servers, value_deserializer=value_deserializer)

