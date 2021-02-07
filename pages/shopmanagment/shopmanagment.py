from flask import Blueprint, render_template, request, redirect
from utilities.db.db_manager import dbManager

# orderManagment blueprint definition
shopmanagment = Blueprint('shopmanagment', __name__, static_folder='static', static_url_path='/shopmanagment', template_folder='templates')


# Routes
@shopmanagment.route('/shopmanagment<int:shop_id>', methods=['GET', 'POST'])
def index(shop_id):
    if request.method == "GET":
        query_result = dbManager.get_orders()
        return render_template('shopmanagment.html', shop_id=shop_id, orders=query_result)
