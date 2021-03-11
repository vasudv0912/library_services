from homi import App, Server
from homi.extend.service import reflection_service, health_service
from models import Book
import sqlalchemy
from library_pb2 import _LIBRARY
from sqlalchemy.orm import sessionmaker
from utils import AlchemyEncoder


engine = sqlalchemy.create_engine(
    'mysql://lab:osmentos@mysqldb:3306/library', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

app = App(
    services=[
        _LIBRARY,
        reflection_service,
        health_service,
    ]
)
service_name = 'library.Library'


# unary-unary method
@app.method(service_name)
def GetBookDetails(book_id):
    book = session.query(Book).filter_by(
            id=book_id).first()
    print(json.dumps(book, cls=AlchemyEncoder))

    return json.dumps(book, cls=AlchemyEncoder)

@app.method(service_name)
def GetAvailableBooks():
	books=session.query(Book).filter_by(is_available=True).all()
	return json.dumps(books, cls=AlchemyEncoder)

if __name__ == '__main__':
    server = Server(app)
    server.run()