from flask import Blueprint, render_template, request, redirect
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

# addnewproduct blueprint definition
addnewproduct = Blueprint('addnewproduct', __name__, static_folder='static', static_url_path='/addnewproduct', template_folder='templates')

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


