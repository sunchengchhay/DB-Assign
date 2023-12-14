from app.extensions import db


# Book Model
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category_id = db.Column(db.ForeignKey('category.id'))
    author_id = db.Column(db.ForeignKey('author.id'))
    language_id = db.Column(db.ForeignKey('language.id'))
    title = db.Column(db.String(200))
    publication_date = db.Column(db.String(200))
    available = db.Column(db.Boolean)

    category = db.relationship('Category', back_populates='books')
    author = db.relationship('Author', back_populates='books')
    language = db.relationship('Language', back_populates='book')


# Category Model
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))

    books = db.relationship('Book', back_populates='category')


# Author Model
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    gender = db.Column(db.String(30))
    date_of_birth = db.Column(db.Date)
    nationality = db.Column(db.String(100))

    books = db.relationship('Book', back_populates='author')


# Language Model
class Language(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))

    book = db.relationship('Book', back_populates='language')
