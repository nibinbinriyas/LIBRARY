from flask import render_template,redirect,url_for
from library import db,app
from library.models import Book
from library.forms import AddForm, DelForm, SearchForm

@app.route('/')
def index():
    books = Book.query.all()
    return render_template('home.html',books=books)



@app.route('/add',methods=['GET','POST'])
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data
        auther = form.auther.data

        book_data = Book(name,auther)
        db.session.add(book_data)
        db.session.commit()

        return redirect(url_for('index'))

    return render_template('add.html',form=form)


@app.route('/search',methods=['GET','POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        auther = form.auther.data
        book_data = Book.query.all()

        return render_template('auther_books.html',book_data=book_data,auther=auther)
    return render_template('search.html',form=form)



@app.route('/delete',methods=['GET','POST'])
def delete():
    form = DelForm()

    if form.validate_on_submit():

        id = form.id.data
        book = Book.query.get(id)
        db.session.delete(book)
        db.session.commit()
        return redirect(url_for('index'))

    return render_template('delete.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)