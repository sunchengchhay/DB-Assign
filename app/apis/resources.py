from flask_restx import Namespace, Resource, reqparse, inputs
from app.models import *
from app.extensions import db
from sqlalchemy import exc

from app.apis.models import *

# Catgory Namespace
category_ns = Namespace(
    "Category Management", description='Manage Category Endpoint', path='/')


put_category_parser = reqparse.RequestParser()
put_category_parser.add_argument(
    'name', type=str, required=True, help='category name is required')


@category_ns.route('/categories')
class Categories(Resource):

    @category_ns.marshal_list_with(output_category_model)
    def get(self):
        """Get all Category Data"""
        categories = Category.query.all()
        if categories:
            return categories, 200
        return {"msg": "not found"}, 404

    @category_ns.expect(put_category_parser)
    def post(self):
        """Create a Category Data"""
        args = put_category_parser.parse_args()

        category = Category(**args)
        try:
            db.session.add(category)
            db.session.commit()
            return {"msg": "add successfully"}, 200

        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500


@category_ns.route('/categories/<int:id>')
class Categoryy(Resource):

    @category_ns.marshal_with(output_category_model)
    def get(self, id):
        """Get a Category Data By ID"""
        try:
            category = Category.query.get(id)
            if category:
                return category, 200
            return {'msg': 'not found'}, 404

        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500

    @category_ns.expect(put_category_parser)
    @category_ns.doc(params={'id': 'Enter ID to Update'})
    def put(self, id):
        """Update a Category Data By ID"""
        args = put_category_parser.parse_args()
        category_name = args['name']
        try:
            category = Category.query.get(id)
            if category:
                category.name = category_name
                db.session.commit()
                return {"msg": "updated"}, 200
            return {"msg": "not found"}, 404

        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500

    @category_ns.doc(params={'id': 'Enter ID to Delete Category'})
    def delete(self, id):
        """Delete a Category Data By ID"""
        try:
            category = Category.query.get(id)
            if category:
                db.session.delete(category)
                db.session.commit()
                return {"msg": "deleted"}, 200
            return {"msg": "not found"}, 404

        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500


# Author Namespace
author_ns = Namespace("Author Management",
                      description='Manage Author Endpoint', path='/')

put_author_parser = reqparse.RequestParser()
put_author_parser.add_argument(
    'gender', type=str, required=True, help='gender required', choices=['Male', 'Female']
)
put_author_parser.add_argument(
    'nationality', type=str, required=True, help='nationality required'
)
put_author_parser.add_argument(
    'date_of_birth', type=inputs.date, help="born date (YYYY-MM-DD)"
)
put_author_parser.add_argument(
    'name',  type=str, help="author full name"
)


@author_ns.route('/authors')
class Authors(Resource):

    @author_ns.expect(put_author_parser)
    def post(self):
        """Create a Author Data"""
        args = put_author_parser.parse_args()
        try:
            author = Author(**args)
            db.session.add(author)
            db.session.commit()
            return {"msg": "added"}, 201
        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500

    @author_ns.marshal_list_with(output_author_model)
    def get(self):
        """Get all Author Data"""
        try:
            authors = Author.query.all()
            if authors:
                return authors, 200
            return {"msg": "not found"}, 404
        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500


@author_ns.route('/authors/<int:id>')
class Authorr(Resource):

    @author_ns.marshal_with(output_author_model)
    def get(self, id):
        """Get a Author Data"""
        try:
            author = Author.query.get(id)
            if author:
                return author, 200
            return {"msg": "not found"}, 404
        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500

    @author_ns.expect(put_author_parser)
    def put(self, id):
        """Update a Author Data"""
        args = put_author_parser.parse_args()
        name = args['name']
        dob = args['date_of_birth']
        nationality = args['nationality']
        gender = args['gender']
        try:
            author = Author.query.get(id)
            if author:
                author.name = name
                author.date_of_birth = dob
                author.nationality = nationality
                author.gender = gender
                db.session.commit()
                return {"msg": "updated"}, 200
            return {"msg": "not found"}, 404
        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500

    def delete(self, id):
        """Delete a Author Data"""
        try:
            author = Author.query.get(id)
            if author:
                db.session.delete(author)
                db.session.commit()
                return {"msg": "deleted"}, 204
            return {"msg": "not found"}, 404
        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500


# Book Namespace
book_ns = Namespace("Book Management",
                    description='Manage Book Endpoint', path='/')

put_book_parser = reqparse.RequestParser()
put_book_parser.add_argument(
    'category_id', type=int, help='category id is required', required=True, default=1
)
put_book_parser.add_argument(
    'author_id', type=int, help='author id is required', required=True, default=1,
)
put_book_parser.add_argument(
    'language', type=str, help='language is required', required=True, default="Khmer",
)
put_book_parser.add_argument(
    'title', type=str, help='title is required', required=True, default="This is the title section",
)
put_book_parser.add_argument(
    'publication_date', type=inputs.date, default="2023-12-31", help='publication_date (YYYY-MM-DD)', required=True
)
put_book_parser.add_argument(
    'available', type=bool, default=True, help='Available is required', choices=[True, False], required=True
)


@book_ns.route('/books')
class Books(Resource):

    @book_ns.marshal_list_with(output_book_model)
    def get(self):
        """Get all Book Data"""
        try:
            books = Book.query.all()
            if books:
                return books, 200
            return {"msg": "not found"}, 404
        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500

    @book_ns.expect(put_book_parser)
    def post(self):
        """Create a Book Data"""
        args = put_book_parser.parse_args()
        try:
            book = Book(**args)
            db.session.add(book)
            db.session.commit()
            return {"msg": "added"}, 201
        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500


@book_ns.route('/books/<int:id>')
class Bookk(Resource):

    @book_ns.marshal_with(output_book_model)
    @book_ns.doc(params={'id': 'Enter ID to Search Book'})
    def get(self, id):
        """Get a Book Data By ID"""
        try:
            book = Book.query.get(id)
            if book:
                return book, 200
            return {"msg": "not found"}, 404

        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500

    @book_ns.expect(put_book_parser)
    @book_ns.doc(params={'id': 'Enter ID to Update Book'})
    def put(self, id):
        """Updated a Book Data By ID"""
        args = put_book_parser.parse_args()
        category_id = args['category_id']
        author_id = args['author_id']
        language = args['language']
        title = args['title']
        publication_date = args['publication_date']
        available = args['available']
        try:
            book = Book.query.get(id)
            if book:
                book.category_id = category_id
                book.author_id = author_id
                book.language = language
                book.title = title
                book.publication_date = publication_date
                book.available = available
                db.session.commit()
                return {"msg": "updated"}, 200
            return {"msg": "not found"}, 404

        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500

    @book_ns.doc(params={'id': 'Enter ID to Delete Book'})
    def delete(self, id):
        """Delete a Book Data By ID"""
        try:
            book = Book.query.get(id)
            if book:
                db.session.delete(book)
                db.session.commit()
                return {"msg": "deleted"}, 204
            return {"msg": "not found"}, 404

        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500
