from flask import Blueprint, render_template, request, redirect
from utilities.db.db_manager import dbManager


# managment blueprint definition
managment = Blueprint('managment', __name__, static_folder='static', static_url_path='/managment', template_folder='templates')


# Routes
@managment.route('/managment', defaults={'option': 1})
@managment.route('/managment/<int:option>', methods=['GET'])
def index(option):
    return render_template('managment.html', option=option)

