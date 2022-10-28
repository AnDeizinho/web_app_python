from flask import Flask
from flask_bootstrap import Bootstrap5

app = Flask(__name__)

bootstrap = Bootstrap5(app)

from controller import home_controller, contacts_controller

def create_app():
    return app