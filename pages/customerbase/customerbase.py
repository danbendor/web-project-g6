from flask import Blueprint, render_template, request, redirect
from utilities.db.db_manager import dbManager

# orderManagment blueprint definition
customerbase = Blueprint('customerbase', __name__, static_folder='static', static_url_path='/customerbase', template_folder='templates')


# Routes
@customerbase.route('/customerbase', methods=['GET', 'POST'])
def index():
    query_result = dbManager.get_orders()
    return render_template('customerbase.html', orders=query_result)
