from flask_restful import Resource, reqparse, fields
from src.app.appctx import result
from src.app.libs import todo_data
from datetime import datetime


class Delete(Resource):
    def delete(self, id):
        flag = False
        now = datetime.now()
        for i in todo_data:
            if int(id) == i['id']:
                flag = True
                i['deleted_at'] = now.strftime("%d-%m-%Y  %H:%M:%S")
                break
        if not flag:
            return result.response(400, message="Data not found")
        return result.response(200, message="Successfuly deleted")
   
    