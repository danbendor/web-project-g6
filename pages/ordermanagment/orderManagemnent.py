from flask import Blueprint, render_template, request, redirect , Response
import xlwt
from utilities.db.db_manager import dbManager
import pymysql
import io
from app import app
import mysql.connector


# orderManagment blueprint definition
orderManagement = Blueprint('orderManagment', __name__, static_folder='static', static_url_path='/orderManagment', template_folder='templates')


# Routes
@orderManagement.route('/orderManagement', methods=['GET', 'POST'])
def index():
     query_result = dbManager.get_orders()
     return render_template('orderManagement.html', orders=query_result)

