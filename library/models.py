from library import db

class Book(db.Model):
    __tablename__ = 'books'

    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    auther = db.Column(db.Text)


    def __init__(self,name,auther):
        self.name = name
        self.auther = auther

       
