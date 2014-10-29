__author__ = 'paultrelease'

from app import app


@app.route('/')
@app.route('/index')
def index():
    return "add /sp to the url use the blueprint"



