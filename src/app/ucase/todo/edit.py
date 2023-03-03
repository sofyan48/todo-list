from flask_restful import Resource, reqparse, fields
from src.app.appctx import result, data
from src.app.libs import todo_data
from datetime import datetime


class Update(Resource):
    def put(self, id):
        payload = data.cast_json()
        now = datetime.now()
        response = {}
        flag = False
        for i in todo_data:
            if int(id) == i['id'] and i['deleted_at'] is None:
                flag = True
                i['title'] = payload['title']
                i['description'] = payload['description']
                i['status'] = payload['status']
                i['updated_at'] = now.strftime("%d-%m-%Y  %H:%M:%S")
                response = i
                break
        if not flag:
            return result.response(400, message="Data not found")
        return result.response(200, message="Data updated", data=response)
   
    