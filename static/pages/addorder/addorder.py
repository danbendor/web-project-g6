from flask import Blueprint, render_template, request, session, redirect
from utilities.db.db_manager import dbManager
import datetime


# addorder blueprint definition
addorder = Blueprint('addorder', __name__, static_folder='static', static_url_path='/addorder', template_folder='templates')


# Routes
@addorder.route('/addorder', methods=['GET', 'POST'])
def index():
        if request.method == 'POST':
                OrderNumber = request.form['OrderNumber']
                fullname = request.form['fullname']
                phone = request.form['phone']
                anotherphonenumber = request.form['anotherphonenumber']
                City = request.form['City']
                Area = request.form['Area']
                Address = request.form['Address']
                Numberofproductspurchased = request.form['Numberofproductspurchased']
                model = request.form['model']
                quantity = request.form['quantity']
                size = request.form['size']
                cloth = request.form['cloth']
                price = request.form['price']
                comment = request.form['comment']
                now = datetime.datetime.utcnow()
                time = now.strftime('%Y-%m-%d')
                check = dbManager.get_customerphone(phone)
                if check:
                        ## need to add update
                        print('customer exsist')
                else:
                        dbManager.create_new_customer(fullname, phone, anotherphonenumber, City, Address, session['employee_id'])
                dbManager.create_new_orders(OrderNumber, time, 'new', comment, price, phone)
                dbManager.create_new_product_in_order(10, OrderNumber, size, cloth, quantity, comment)
                return redirect('orderManagement')
        return render_template('add order.html')


