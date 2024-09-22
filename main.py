#import sqlite3
from flask import Flask, render_template, request, redirect, url_for
from app import db, app
from models import Book
from flask_wtf import CSRFProtect
from forms import MyForms




app.config['SECRET_KEY'] = 'thisisasecretkey'
csrf = CSRFProtect(app)


@app.route('/', methods=['GET', 'POST'])
@csrf.exempt
def home():
    if request.method == 'GET':
        books = Book.query.all()
        book = [x for x in books]
        print(book)
    return render_template("index.html", books=books)



@app.route('/add', methods=['GET', 'POST'])
def add():
    form = MyForms()
    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        rating = form.rating.data
        review = form.review.data
        new_book = Book(title=title, author=author, rating=rating, review=review)
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template("add.html", form=form)


if __name__=="__main__":
    app.run(debug=True)
























"""
#create connection to the database
db = sqlite3.connect("books-collection.db")
# create a cursor object
cursor = db.cursor()

# create a table
cursor.execute(""
    CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title VARCHAR(250) NOT NULL UNIQUE,
        author VARCHAR(250) NOT NULL,
        rating FLOAT NOT NULL
    )
"")


# insert data
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
cursor.execute("INSERT INTO books VALUES(2, 'The Lord of the Rings', 'J. R. R. Tolkien', '9.2')")
cursor.execute("INSERT INTO books VALUES(3, 'Angels and Demons', 'Dan Brown', '8.3')")
db.commit()
"""