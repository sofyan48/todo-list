from datetime import datetime

now = datetime.now()

todo_data = [
    {
        "id": 1,
        "title": "Soulparking Test",
        "description": "Testing python on 7 days",
        "status": "on-progress",
        "is_finish": False,
        "created_at": now.strftime("%d-%m-%Y  %H:%M:%S"),
        "updated_at": now.strftime("%d-%m-%Y  %H:%M:%S"),
        "deleted_at": None
    },
    {
        "id": 2,
        "title": "Python Test",
        "status": "on-progress",
         "is_finish": False,
        "description": "Testing python on flask",
        "created_at": now.strftime("%d-%m-%Y  %H:%M:%S"),
        "updated_at": now.strftime("%d-%m-%Y  %H:%M:%S"),
        "deleted_at": None
    }
]