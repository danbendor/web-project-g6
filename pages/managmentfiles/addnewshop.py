from flask import Blueprint, render_template, request, redirect, url_for
from settings import DB
import mysql.connector
from utilities.db.db_manager import dbManager

# addnewshop blueprint definition
addnewshop = Blueprint('addnewshop', __name__, static_folder='static', static_url_path='/addnewshop',
                       template_folder='templates')

# Routes
@addnewshop.route('/addnewshop', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        shop_id = request.form['shop_id']
        shop_name = request.form['shop_name']
        city = request.form['city']
        phone = request.form['phone']
        dbManager.create_new_shop(shop_id, shop_name, city, phone)
        return render_template('Managment.html')
    else:
        return render_template('addnewshop.html')


# updateorderstatus blueprint definition
updateorderstatus = Blueprint('updateorderstatus', __name__, static_folder='static',
                              static_url_path='/updateorderstatus', template_folder='templates')

updatecustomer = Blueprint('updatecustomer', __name__, static_folder='static',
                              static_url_path='/updatecustomer', template_folder='templates')

updateproductprice = Blueprint('updateproductprice', __name__, static_folder='static',
                              static_url_path='/updateproductprice', template_folder='templates')

# addnewproduct blueprint definition
addnewproduct = Blueprint('addnewproduct', __name__, static_folder='static', static_url_path='/addnewproduct',
                          template_folder='templates')


# deleteorder blueprint definition
deleteorder = Blueprint('deleteorder', __name__, static_folder='static', static_url_path='/deleteorder',
                          template_folder='templates')


# storessales blueprint definition
storessales = Blueprint('storessales', __name__, static_folder='static', static_url_path='/storessales',
                        template_folder='templates')


# Routes
@addnewproduct.route('/addnewproduct', methods=['GET', 'POST'])
def index1():
    if request.method == 'POST':
        product_id = request.form['product_id']
        product_name = request.form['product_name']
        product_type = request.form['product_type']
        product_price = request.form['product_price']
        dbManager.create_new_product(product_id, product_name, product_type, product_price)
        return render_template('Managment.html')
    else:
        return render_template('addnewproduct.html')


@updateorderstatus.route('/updateorderstatus', methods=['GET', 'POST'])
def index2():
    if request.method == 'GET':
        order_id = request.args['order_id']
        status = request.args['status']
        dbManager.update_orders(order_id, status)
        return render_template('Managment.html')
    else:
        return render_template('addnewproduct.html')


@updatecustomer.route('/updatecustomer', methods=['GET', 'POST'])
def index2():
    if request.method == 'GET':
        customer_phone = request.args['customer_phone']
        customer_address = request.args['customer_address']
        customer_city = request.args['customer_city']
        dbManager.updade_customerAddress(customer_phone, customer_city, customer_address)
        return render_template('Managment.html')
    else:
        return render_template('updatecustomer.html')


@updateproductprice.route('/updateproductprice', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        product_id = request.args['product_id']
        product_price = request.args['product_price']
        dbManager.update_product_price(product_id, product_price)
        return render_template('Managment.html')
    else:
        return render_template('updatecustomer.html')



@deleteorder.route('/deleteorder', methods=['GET'])
def index():
    if request.method == 'GET':
        order_id = request.args['order_id']
        dbManager.delete_product_in_order(order_id)
        dbManager.delete_order(order_id)
        return render_template('Managment.html')
    else:
        return render_template('deleteorder.html')
