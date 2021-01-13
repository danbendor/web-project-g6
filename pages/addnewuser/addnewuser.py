from flask import Blueprint, render_template, request, redirect
from settings import DB
import mysql.connector
from utilities.db.db_manager import dbManager


# addnewuser blueprint definition
addnewuser = Blueprint('addnewuser', __name__, static_folder='static', static_url_path='/addnewuser', template_folder='templates')

# Routes
@addnewuser.route('/addnewuser', methods=['GET', 'POST'])
def index1():
    query_result = dbManager.shop_id()
    if request.method == 'POST':
        EmployeId = request.form['EmployeId']
        fullname = request.form['fullname']
        user = request.form['user']
        password = request.form['password']
        shop_id = request.form["shop_id"]
        dbManager.create_new_user(EmployeId, fullname, user, password, shop_id)
        return render_template('loginhtml.html', shops=query_result)
    else:
        return render_template('addnewuser.html', shops=query_result)