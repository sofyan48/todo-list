from flask_restful import Resource
from src.app.appctx import result, data
from src.app.libs import todo_data
from datetime import datetime

class Save(Resource):
    def post(self):
        now = datetime.now()
        payload = data.cast_json()
        todo_save = {
            "id": len(todo_data)+1,
            "title": payload['title'],
            "description": payload['description'],
            "status": False,
            "is_finish": False,
            "created_at": now.strftime("%d-%m-%Y  %H:%M:%S"),
            "updated_at": now.strftime("%d-%m-%Y  %H:%M:%S"),
            "deleted_at": None
        }

        todo_data.append({
            "id": len(todo_data)+1,
            "title": payload['title'],
            "description": payload['description'],
            "status": payload['status'],
            "is_finish": False,
            "created_at": now.strftime("%d-%m-%Y  %H:%M:%S"),
            "updated_at": now.strftime("%d-%m-%Y  %H:%M:%S"),
            "deleted_at": None
        })

        return result.response(200, message="OK", data=todo_save)
   
    