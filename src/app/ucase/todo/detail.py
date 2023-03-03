from flask_restful import Resource, reqparse, fields
from src.app.appctx import result
from src.app.libs import todo_data

class Detail(Resource):
    def get(self, id):
        response = {}
        flag = False
        for i in todo_data:
            if int(id) == i['id'] and i['deleted_at'] is None:
                flag = True
                response = i
                break
        if not flag:
            return result.response(400, message="Data not found")
        return result.response(200, message="OK", data=response)
   
    