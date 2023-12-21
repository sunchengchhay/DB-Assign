from app.extensions import db


# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.ForeignKey('category.id'))
    author_id = db.Column(db.ForeignKey('author.id'))
    language = db.Column(db.String(50))
    title = db.Column(db.String(200))
    publication_date = db.Column(db.Date)
    available = db.Column(db.Boolean)

    category = db.relationship('Category', back_populates='books')
    author = db.relationship('Author', back_populates='books')


# Category Model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    books = db.relationship('Book', back_populates='category')


# Author Model
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    gender = db.Column(db.String(200))
    date_of_birth = db.Column(db.Date)
    nationality = db.Column(db.String(50))

    books = db.relationship('Book', back_populates='author')
