from flask import Blueprint, render_template, redirect, url_for, request, session, flash
from utilities.db.db_manager import dbManager


# homepage blueprint definition
homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage', template_folder='templates')


# Routes
@homepage.route('/', methods=['GET', 'POST'])
def index():
    session['Logged_in'] = False
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        check = dbManager.get_user_and_password(username, password)
        if check == True:
            user_id = dbManager.get_employee_id(username, password)
            user_name = dbManager.get_employee_name(username, password)
            session['Logged_in'] = True
            session['employee'] = True
            session['customer'] = False
            session['employee_id'] = user_id
            session['employee_name'] = user_name
            return redirect('/orderManagement')
    return render_template('loginhtml.html')

