from library.models import Book
from library import db

def test_Book():
    newbook = Book('Half girl friend','Chetan Bagat')

    db.session.add(newbook)
    db.session.commit()

    books = Book.query.all()
    for book in books:
        print(book)

    assert (1==1)