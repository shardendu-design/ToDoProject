# import all the necessary library


from app import db
from datetime import date, datetime

# create company databse model


class ToDos(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key=True)
    todo_name = db.Column(db.String(50), unique=True, nullable=False)
    todo_description = db.Column(db.String(50))
    todo_created_date = db.Column(db.DateTime)
    todo_status = db.Column(db.String(50), nullable=False)

    def __init__(self,todo_name,todo_description,todo_created_date,todo_status):

        self.todo_name = todo_name
        self.todo_description = todo_description
        self.todo_created_date = todo_created_date
        self.todo_status = todo_status

    def __reper__(self):
        return 'The name is {}'.format(self.todo_name)
