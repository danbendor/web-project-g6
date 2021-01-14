from flask import Flask, render_template, url_for, redirect, request, session

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## About
from pages.about.about import about
app.register_blueprint(about)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## order managment
from pages.ordermanagment.orderManagemnent import orderManagement
app.register_blueprint(orderManagement)

## detailsorder
from pages.detailsorder.detailsorder import detailsorder
app.register_blueprint(detailsorder)

## addorder
from pages.addorder.addorder import addorder
app.register_blueprint(addorder)

## addnewuser
from pages.addnewuser.addnewuser import addnewuser
app.register_blueprint(addnewuser)

## managment
from pages.managment.managment import managment
app.register_blueprint(managment)

## managment
from pages.contact.contact import contact
app.register_blueprint(contact)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

## addnewshop
from pages.managmentfiles.addnewshop import addnewshop
app.register_blueprint(addnewshop)

from pages.managmentfiles.addnewshop import addnewproduct
app.register_blueprint(addnewproduct)

from pages.managmentfiles.addnewshop import storessales
app.register_blueprint(storessales)

from pages.managmentfiles.addnewshop import updateorderstatus
app.register_blueprint(updateorderstatus)

from pages.customerlogin.customerlogin import customerlogin
app.register_blueprint(customerlogin)

contact
###### Components
## Main menu
from components.main_menu.main_menu import main_menu
app.register_blueprint(main_menu)

from pages.customerbase.customerbase import customerbase
app.register_blueprint(customerbase)

if __name__ == 'main':
    app.run(debug=True)
