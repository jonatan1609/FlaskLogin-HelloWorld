from .app import app
from .database import User

from pony.orm import db_session
from flask_login import login_required, login_user, logout_user, current_user
from flask import request
from hashlib import sha1

FIELDS = "username", "password"


@app.route('/login')  # login endpoint
def login():
    if any(field not in request.args for field in FIELDS):
        return "You have to specify arguments username & password!"

    username, password = request.args.get("username"), request.args.get("password")
    with db_session:
        user = User.get(username=username, password=sha1(password.encode()).hexdigest())
        if not user:
            return "User is not existing!"
    if not login_user(user):
        return "something went wrong!"
    return "Signed in successfully!"


@app.route('/signup')  # signup endpoint
def signup():
    if any(field not in request.args for field in FIELDS):
        return "You have to specify arguments username & password!"

    username, password = request.args.get("username"), request.args.get("password")
    with db_session:
        if User.get(username=username):
            return "User is already existing!"
        User(username=username, password=sha1(password.encode()).hexdigest())
    return "Signed up successfully!"


@app.route('/logout')  # logout endpoint
@login_required
def logout():
    logout_user()
    return "Logged out successfully!"


@app.route('/')
@login_required
def main():
    return "Hi! " + current_user.username
