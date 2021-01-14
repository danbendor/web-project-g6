from flask import Blueprint, render_template, redirect, url_for, request, session
from utilities.db.db_manager import dbManager

# homepage for customer blueprint definition
customerlogin = Blueprint('customerlogin', __name__, static_folder='static', static_url_path='/customerlogin', template_folder='templates')

# Routes
@customerlogin.route('/customerlogin', methods=['GET', 'POST'])
def index():
    session['Logged_in'] = False
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        check1 = dbManager.get_order_and_phone(username, password)
        if check1 == True:
            user_name = dbManager.get_customer_name(password)
            session['Logged_in'] = True
            session['customer'] = True
            session['employee'] = False
            session['order_id'] = int(username)
            session['user_name'] = user_name
            session['phone'] = password
            return redirect('/customerbase')
    return render_template('customerlogin.html')

