
from grpcalchemy import DefaultConfig
from models import Book
import sqlalchemy
from sqlalchemy.orm import sessionmaker
from grpcalchemy.orm import Message, StringField
from grpcalchemy import Server, Context, grpcmethod
from typing import List
from models import Book , Record

engine = sqlalchemy.create_engine(
    'mysql://lab:osmentos@mysqldb:3306/library2', echo=True)
Session = sessionmaker(bind=engine)
session = Session()


class BookDetailsFields(Message):
    book_name: str
    author_name: str
    description: str
    condition: str


class AvailablebookFields(Message):
    book_name: str
    author_name: str


class BookDetailsRequestmesg(Message):
    book_id: int

class AvailableRequestMesg(Message):
	None
class BookRecordRequestMesg(Message):
	book_id: int

class BookDetailsResponseMesg(Message):
	books: List[BookDetailsFields]


class AvailableResponseMesg(Message):
    availablebooks: List[AvailablebookFields]

class BookRecordResponseMesg(Message):
	count: int

class GetBookdetails(Server):
    @grpcmethod
    def bookDetails(self, request: BookDetailsRequestmesg, context: Context) -> BookDetailsResponseMesg:
        book_1 = session.query(Book).filter_by(
            id=request.book_id).first()
        x = BookDetailsFields()
        x.book_name = book_1.book_name
        x.author_name = book_1.author_name
        x.description = book_1.description
        x.condition = book_1.condition
        return BookDetailsResponseMesg(books=[x])

    @grpcmethod
    def availableBooks(self, request: AvailableRequestMesg , context: Context) -> AvailableResponseMesg:
        available_book = session.query(Book).filter_by(
            is_available=True).all()
        arr = []
        for book in available_book:
        	x = AvailablebookFields()
        	x.book_name = book.book_name
        	x.author_name = book.author_name
        	arr.append(x)
        return AvailableResponseMesg(availablebooks=arr)

    @grpcmethod
    def bookRecord(self, request:BookRecordRequestMesg , context: Context) -> BookRecordResponseMesg:
    	issuecount=session.query(Record).filter_by(
            id=request.book_id).count()
    	return BookRecordResponseMesg(count=issuecount)


class TestConfig(DefaultConfig):
    GRPC_SEVER_REFLECTION_ENABLE = True


if __name__ == '__main__':
    GetBookdetails.run(host="library", port=50059, config=TestConfig())
