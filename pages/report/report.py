from flask import Blueprint, render_template, request, redirect, session
from utilities.db.db_manager import dbManager
import datetime


# report blueprint definition
report = Blueprint('report', __name__, static_folder='static', static_url_path='/report', template_folder='templates')

# Routes
@report.route('/report', defaults={'option': 1})
@report.route('/report/<int:option>', methods=['GET'])
def index(option):
    query_result = dbManager.get_storessales()
    query_result2 = dbManager.get_salesByProducets()
    query_result3 = dbManager.get_user_orders(session['employee_id'])
    return render_template('report.html', option=option, prices=query_result, productssales=query_result2, orders=query_result3)

