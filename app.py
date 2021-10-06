import os
from flask import render_template,redirect,url_for,request,flash
from library import db,app
from library.models import Book,User
from library.forms import AddForm, DelForm, SearchForm,LoginForm,RegistrationForm
from flask_login.utils import login_required, login_user, logout_user




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
        price = form.price.data
        image = form.image.data

        book_data = Book(name,auther,price,image)
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


    

















@app.route('/')
def home():
    return render_template('home.html')

@app.route('/welcome')
@login_required
def welcome_user():
    return render_template("welcome_user.html")

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("You are logged out")
    return redirect(url_for('home'))



@app.route('/login',methods=['GET','POST'])
def login():
    
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        if user.check_password(form.password.data) and user is not None:
            
            login_user(user)
            flash('Logged in successfully')

            next = request.args.get('next')

            if next == None or not next[0] == '/':
                next = url_for('welcome_user')
            return redirect(next)

    return render_template('login.html',form=form)

@app.route('/register',methods=['GET','POST'])
def register():

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(email=form.email.data,
                    username=form.username.data,
                    password=form.password.data)
        
        db.session.add(user)
        db.session.commit()
        flash('Successfully Registered!')

        return redirect(url_for('login'))
    
    return render_template('register.html',form=form)


















if __name__ == '__main__':
    
    port = int(os.environ.get('PORT',5000))
    app.run(debug=True,host='0.0.0.0',port=port)