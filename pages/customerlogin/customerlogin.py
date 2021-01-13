from flask import Blueprint, render_template, redirect, url_for, request, session
from utilities.db.db_manager import dbManager

# homepage for customer blueprint definition
customerlogin = Blueprint('customerlogin', __name__, static_folder='static', static_url_path='/customerlogin', template_folder='templates')

# Routes
@customerlogin.route('/customerlogin', methods=['GET', 'POST'])
def index():
    if request.method == 'POST' and 'phone' in request.form:
        phone1 = request.form['phone']
        check = dbManager.check_customer_phone(phone1)
        print(check)
        if check == True:
            orderdetails = dbManager.get_ordersdetails1(phone1)
            order_id = orderdetails.order_id
            session['Logged_in'] = True
            print(orderdetails)
            return render_template('', order_id=order_id, orderdetails=orderdetails )
        else:
            return render_template('customerlogin.html')
    return render_template('customerlogin.html')

