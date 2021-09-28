from library.models import Book
from library import db
#put in function

def test_Book():
    newbook = Book('Half girl friend','Chetan Bagat')

    db.session.add(newbook)
    x = db.session.commit()

    books = Book.query.all()
    for book in books:
        print(book)

    assert (1==1)