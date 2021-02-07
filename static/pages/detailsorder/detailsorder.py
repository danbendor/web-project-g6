from flask import Blueprint, render_template, request
from utilities.db.db_manager import dbManager

# detailsorder blueprint definition
detailsorder = Blueprint('detailsorder', __name__, static_folder='static', static_url_path='/detailsorder', template_folder='templates')


# Routes
@detailsorder.route('/detailsorder/<int:orderid>', methods=['GET'])
def index(orderid):
    if request.method == "GET":
        query_result = dbManager.get_ordersdetails(orderid)
        return render_template('detailsorder.html', orderid=orderid, details=query_result)