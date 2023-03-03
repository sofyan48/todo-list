from flask import Blueprint
from flask_restful import Api
from src.app.ucase.health import HealthController
from src.app.ucase import todo

v1_blueprint = Blueprint("api", __name__, url_prefix='/v1')
api = Api(v1_blueprint)

api.add_resource(HealthController, '/health')

api.add_resource(todo.List, '/todo')
api.add_resource(todo.Detail, '/todo/<id>')
api.add_resource(todo.Save, "/todo")
api.add_resource(todo.Delete, "/todo/<id>")
api.add_resource(todo.Update, "/todo/<id>")
api.add_resource(todo.Finish, "/todo/<id>/finish")

