__author__ = 'paultrelease'

from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound


simple_page = Blueprint('simple_page', __name__, template_folder='templates', url_prefix='/sp')

# @simple_page.route('/', defaults={'page': 'index'})
# @simple_page.route('/<page>')
@simple_page.route('/')
# def show(page):
def show():
    try:
        return render_template('success.html')
    except TemplateNotFound:
        abort(404)


