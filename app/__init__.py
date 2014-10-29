from app.try_blueprints.try_blueprints import simple_page

__author__ = 'paultrelease'

from flask import Flask
from app.try_blueprints import try_blueprints

app = Flask(__name__)
app.register_blueprint(simple_page)
from app import server
