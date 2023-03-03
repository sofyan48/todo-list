from flask_restful import Resource, reqparse, fields
from src.app.appctx import result
from src.app.libs import todo_data
from datetime import datetime

class Finish(Resource):
    def get(self, id):
        response = {}
        flag = False
        now = datetime.now()
        for i in todo_data:
            if int(id) == i['id'] and i['deleted_at'] is None:
                flag = True
                i['is_finish'] = True
                i['updated_at'] = now.strftime("%d-%m-%Y  %H:%M:%S")
            else:
                flag = False
                break
        if not flag:
            return result.response(400, message="Data not found")
        return result.response(200, message="Successfully finished", data=response)
   
    