from flask import Blueprint, render_template, request, redirect
from utilities.db.db_manager import dbManager


# managment blueprint definition
managment = Blueprint('managment', __name__, static_folder='static', static_url_path='/managment',
                      template_folder='templates')

# Routes
@managment.route('/managment', defaults={'option': 1})
@managment.route('/managment/<int:option>', methods=['GET'])
def index(option):
    query_result = dbManager.customers_phone()
    query_result2 = dbManager.get_orders()
    query_result3 = dbManager.product_id()
    return render_template('managment.html', option=option, phones_numbers=query_result, orders=query_result2,
                           products=query_result3)

