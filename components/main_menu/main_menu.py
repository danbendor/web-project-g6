from flask import Blueprint, render_template

# main_menu blueprint definition
main_menu = Blueprint('main_menu', __name__, static_folder='static', static_url_path='/main_menu', template_folder='templates')
