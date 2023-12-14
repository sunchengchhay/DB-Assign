from flask_restx import Namespace, Resource, reqparse
from app.models import *
from app.extensions import db
from sqlalchemy import exc

from app.apis.models import output_category_model

category_ns = Namespace(
    "Category Management", description='Manage Category Endpoint', path='/')


put_category_parser = reqparse.RequestParser()
put_category_parser.add_argument(
    'category_name', type=str, required=True, help='category name is required')


@category_ns.route('/categories')
class Categories(Resource):

    @category_ns.marshal_list_with(output_category_model)
    def get(self):
        """Get all Categories"""
        categories = Category.query.all()
        if categories:
            return categories, 200
        return {"msg": "not found"}, 404

    @category_ns.expect(put_category_parser)
    def post(self):
        """Create a Category"""
        args = put_category_parser.parse_args()
        category_name = args['category_name']

        category = Category(name=category_name)
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
        """Get a Category"""
        try:
            category = Category.query.get(id)
            if category:
                return category, 200
            return {'msg': 'not found'}, 404

        except exc.SQLAlchemyError as e:
            return {'msg': str(e.__cause__)}, 500

    def put(self, id):
        pass
