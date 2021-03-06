from os import name
from library.models import Book,User
from library import db

def test_Book():
    newbook = Book('Half girlfriend','Chetan Bhagat','225','https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1407223058l/22874559.jpg')
    
    db.session.add(newbook)
    db.session.commit()


    books = Book.query.all()
    for book in books:
        print(book.name)
        assert (book.name == 'Two States')
        break

    db.session.delete(newbook)
    db.session.commit()


    newuser = User('abc@gmail.com','abc','123')

    db.session.add(newuser)
    db.session.commit()

    users = User.query.all()
    for user in users:
        print(user.username)
        assert(user.username == 'nibi')
        break

    db.session.delete(newuser)
    db.session.commit()
    