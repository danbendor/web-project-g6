from flask import Blueprint, render_template

# orderManagment blueprint definition
contact = Blueprint('contact', __name__, static_folder='static', static_url_path='/contact', template_folder='templates')


# Routes
@contact.route('/contact')
def index():
    return render_template('Contacthtml.html')
