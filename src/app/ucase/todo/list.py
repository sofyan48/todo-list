from flask_restful import Resource, reqparse, fields
from src.app.appctx import result
from src.app.libs import todo_data

class List(Resource):
    def get(self):
        response = []
        for i in todo_data:
            if i['deleted_at'] is None:
                response.append(i)
        return result.response(200, message="OK", data=response)
   
    