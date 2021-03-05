from pony.orm import Database, Required
from pony.flask import Pony
from flask_login import UserMixin
from .app import app, login_manager

db = Database()


class User(db.Entity, UserMixin):
    username = Required(str, unique=True)
    password = Required(str)


db.bind('sqlite', filename="database.sqlite", create_db=True)
db.generate_mapping(create_tables=True)


@login_manager.user_loader  # configuring the login endpoint
def load_user(user_id):
    return User.get(id=user_id)


Pony(app)
