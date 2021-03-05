from flask import Flask, redirect, url_for
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = "my-secret-key-for-flask-login"
login_manager = LoginManager(app)  # binding flask-login into the Flask app

login_manager.login_view = 'login'  # login endpoint


@login_manager.unauthorized_handler
def handle_needs_login():
    return redirect(url_for('login'))
