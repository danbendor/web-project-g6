from flask import Blueprint, render_template, request, redirect, url_for
from settings import DB
import mysql.connector
from utilities.db.db_manager import dbManager

# addnewshop blueprint definition
addnewshop = Blueprint('addnewshop', __name__, static_folder='static', static_url_path='/addnewshop', template_folder='templates')

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
updateorderstatus = Blueprint('updateorderstatus', __name__, static_folder='static', static_url_path='/updateorderstatus', template_folder='templates')


# addnewproduct blueprint definition
addnewproduct = Blueprint('addnewproduct', __name__, static_folder='static', static_url_path='/addnewproduct', template_folder='templates')

# storessales blueprint definition
storessales = Blueprint('storessales', __name__, static_folder='static', static_url_path='/storessales', template_folder='templates')


# Routes
@addnewproduct.route('/addnewproduct', methods=['GET', 'POST'])
def index1():
        if request.method == 'POST':
            product_id = request.form['product_id']
            product_name = request.form['product_name']
            product_type = request.form['product_type']
            product_pic = request.form['product_pic']
            print('sdfn;ks')
            dbManager.create_new_product(product_id, product_name, product_type, product_pic)
            return render_template('Managment.html')
        else:
            return render_template('addnewproduct.html')

@storessales.route('/storessales', methods=['GET', 'POST'])
def index1():
        if request.method == 'GET':
            query_result = dbManager.get_storessales()
            return render_template('storessales.html', prices=query_result)
        else:
            return render_template('addnewproduct.html')

@updateorderstatus.route('/updateorderstatus', methods=['GET', 'POST'])
def index2():
        if request.method == 'GET':
            orderid = request.args['orderid']
            status = request.args['status']
            dbManager.update_orders(orderid, status)
            return render_template('updateorderstatus.html')
        else:
            return render_template('addnewproduct.html')

