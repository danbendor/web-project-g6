from settings import DB
import mysql.connector
from flask import request, render_template


class DBManager:
    __connection = None
    __cursor = None

    def __init__(self):
        pass

    def commit(self, query, args=()):
        # Use for INSERT UPDATE, DELETE statements.
        # Returns: The number of rows affected by the query (a non-negative int).
        self.__connect()
        self.__execute(query, args)
        self.__connection.commit()
        affected_rows = self.__cursor.rowcount
        self.__close_connection()
        return affected_rows

    def fetch(self, query, args=()):
        # Use for SELECT statement.
        # Returns: False if the query failed, or the result of the query if it succeeded.
        query_result = False
        self.__connect()
        if self.__execute(query, args):
            query_result = self.__cursor.fetchall()
        self.__close_connection()
        return query_result

    def execute(self, query, args=()):
        # Use for CREATE, DROP AND ALTER statements.
        self.__connect()
        query_result = self.__execute(query, args)
        self.__close_connection()
        return query_result

    def __connect(self):
        # Opens a connection to the database.
        try:
            if not self.__connection or not self.__connection.is_connected():
                self.__connection = mysql.connector.connect(**DB)
                self.__cursor = self.__connection.cursor(named_tuple=True)
        except mysql.connector.Error as error:
            print("Connection failed with error {}".format(error))

    def __execute(self, query, args=()):
        # Executes a given query with given args, if provided.
        if query:
            try:
                self.__cursor.execute(query, args)
                return True
            except mysql.connector.Error as error:
                print("Query failed with error {}".format(error))
        return False

    def __close_connection(self):
        # Closes an open database connection.
        try:
            if self.__connection.is_connected():
                self.__connection.close()
                self.__cursor.close()
        except mysql.connector.Error as error:
            print("Failed to close connection with error {}".format(error))

    def create_new_user(self, employee_id, employee_name, employee_user, employee_password, shop_id):

        query = "INSERT INTO employees(employee_id , employee_name, employee_user, employee_password, shop_id) VALUES ('%s', '%s', '%s', '%s', '%s')" % (
            employee_id, employee_name, employee_user, employee_password, shop_id)
        #self.interact_db(query, 'commit')
        self.commit(query)
        return

    def create_new_customer(self, fullname, phone, anotherphonenumber, City, Address, Email, employee_id ):

        query = "INSERT INTO customers( customer_name, customer_phone, customer_extraphone, customer_city, customer_address, customer_email, employee_id) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (
            fullname, phone, anotherphonenumber, City, Address, Email, employee_id)
        self.commit(query)
        return

    def get_customerphone(self, phone):
        query = "select * from customers"
        query_result = self.fetch(query)
        for que in query_result:
            if que.customer_phone == phone:
                return True
        return False

    def get_orders(self):
        query = "select orders.order_id, customers.customer_name, customers.customer_city, orders.order_date, orders.order_status,orders.order_price from orders inner join customers on orders.customer_phone=customers.customer_phone  "
        # query_result = self.interact_db(query, query_type='fetch')
        query_result = self.fetch(query)
        return query_result

    def get_user_and_password(self, user, password):
        query = "select employees.employee_user, employees.employee_password from employees"
        #query_result = self.interact_db(query, query_type='fetch')
        query_result = self.fetch(query)
        for que in query_result:
            if que.employee_user == user and que.employee_password == password:
                return True
        return False

    def get_order_and_phone(self, user, password):
        query = "select orders.order_id, orders.customer_phone from orders"
        #query_result = self.interact_db(query, query_type='fetch')
        query_result = self.fetch(query)
        for que in query_result:
            if que.order_id == int(user) and que.customer_phone == password:
                return True
        return False

    def get_employee_id(self, user, password):
        query = "select employees.employee_id ,employees.employee_user, employees.employee_password from employees"
        #query_result = self.interact_db(query, query_type='fetch')
        query_result = self.fetch(query)
        for que in query_result:
            if que.employee_user == user and que.employee_password == password:
                return que.employee_id
        return 0

    def get_employee_name(self, user, password):
        query = "select employees.employee_name ,employees.employee_user, employees.employee_password from employees"
        #query_result = self.interact_db(query, query_type='fetch')
        query_result = self.fetch(query)
        for que in query_result:
            if que.employee_user == user and que.employee_password == password:
                return que.employee_name
        return 0

    def get_customer_name(self, phone):
        query = "select customers.customer_name, customers.customer_phone from customers"
        # query_result = self.interact_db(query, query_type='fetch')
        query_result = self.fetch(query)
        print(query_result)
        print(phone)
        for que in query_result:
            if que.customer_phone == phone:
                return que.customer_name
        return 0


    def create_new_shop(self, shop_id, shop_name, shop_city, shop_phone):

        query = "INSERT INTO shops( shop_id, shop_name, shop_city, shop_phone) VALUES ( '%s', '%s', '%s', '%s')" % (
            shop_id, shop_name, shop_city, shop_phone)
        #self.interact_db(query, 'commit')
        self.commit(query)
        return

    def create_new_product(self, product_id, product_name, product_type, product_pic):

        query = "INSERT INTO products( product_id, product_name, product_type, product_pic) VALUES ( '%s', '%s', '%s', '%s')" % (
            product_id, product_name, product_type, product_pic)
        self.commit(query)
        return

    def create_new_orders(self, order_id, order_date, order_status, order_comment, order_price, customer_phone):

        query = "INSERT INTO orders( order_id, order_date, order_status, order_comment,order_price,customer_phone) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (
            order_id, order_date, order_status, order_comment, order_price, customer_phone)
        self.commit(query)
        return

    def create_new_product_in_order(self, product_id, order_id, size, color, quantity, comment):

        query = "INSERT INTO product_in_order( product_id, order_id, size, color,quantity, comment) VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" % (
            product_id, order_id, size, color, quantity, comment)
        self.commit(query)
        return

    def get_ordersdetails(self, order_id):
        query = "select orders.order_id,orders.order_status, customers.customer_name, customers.customer_city, customers.customer_address, customers.customer_phone  ,orders.order_date, orders.order_price, products.product_type, products.product_name, product_in_order.size, product_in_order.color, product_in_order.comment from customers inner join orders " \
                "on orders.customer_phone = customers.customer_phone  inner join  product_in_order on orders.order_id=product_in_order.order_id inner join  products on products.product_id=product_in_order.product_id  "
        query_result = self.fetch(query)
        for que in query_result:
            if que.order_id == order_id:
                return que
        return

    def get_ordersbyshop(self, shop_id):
        query = "select orders.order_id, customers.customer_name, customers.customer_city, orders.order_date," \
                " orders.order_price, employees.shop_id from orders inner join customers on orders.customer_phone=customers.customer_phone inner join employees on customers.employee_id=employees.employee_id "
        query_result =self.fetch(query)
        for que in query_result:
            if que.shop_id == shop_id:
                return que

    def get_ordersbystatus(self, status):
        query = "select orders.order_id, customers.customer_name, customers.customer_city, orders.order_date, orders.order_price, orders.order_status from orders inner join customers on orders.customer_phone=customers.customer_phone"
        query_result = self.fetch(query)
        for que in query_result:
            if que.order_status == status:
                return que

    def check_customer_phone(self, phone):
        query = "select customers.customer_phone from customers"
        query_result = self.fetch(query)
        for que in query_result:
            if que.customer_phone == phone:
                return True
        return False



    def get_customer_phone(self, phone):
        query = "select customers.customer_phone from customers"
        query_result = self.fetch(query)
        for que in query_result:
            if que.customer_phone == phone:
                return que.customer_phone
        return "x"

    def get_ordersdetails1(self, phone):
        query = "select orders.order_id,orders.order_status, customers.customer_name, customers.customer_city, customers.customer_address, customers.customer_phone  ,orders.order_date, orders.order_price, products.product_type, products.product_name, product_in_order.size, product_in_order.color, product_in_order.comment from customers inner join orders " \
                "on orders.customer_phone = customers.customer_phone  inner join  product_in_order on orders.order_id=product_in_order.order_id inner join  products on products.product_id=product_in_order.product_id  "
        query_result = self.fetch(query)
        for que in query_result:
            if que.customer_phone == phone:
                return que

    def updade_customer(self, phone, city, address, email):
        query = "UPDATE customers SET customer_city=%s, customer_address=%s, customer_email=%s  where customer_phone=%s" % (city, address, email, phone)
        query_result = self.commit(query)
        return

    def get_ordersearch(self, search):
        query = "select orders.order_id, customers.customer_name, customers.customer_city, orders.order_date, orders.order_status, orders.order_price from orders inner join customers on orders.customer_phone=customers.customer_phone"
        query_result = self.fetch(query)
        for que in query_result:
            if que.order_id == search:
                return que
            if que.customer_name == search:
                return que
            if que.customer_city == search:
                return que
            if que.order_status == search:
                return que

        return 0

    def shop_id(self):
        query = "select DISTINCT shop_id from  shops"
        query_result = self.fetch(query)
        return query_result

    def product_id(self):
        query = "select DISTINCT product_id from  products"
        query_result = self.fetch(query)
        return query_result

    def get_storessales(self):
        query = "select sum(orders.order_price) as totalsum, shops.shop_name  from orders inner join customers on orders.customer_phone = customers.customer_phone  inner join  employees on customers.employee_id=employees.employee_id inner join shops on employees.shop_id = shops.shop_id GROUP BY  employees.shop_id"
        query_result = self.fetch(query)
        return query_result

    def update_orders(self, order_status, order_id):
        query = "UPDATE orders SET order_status = %s WHERE order_id =%s" % (order_status, order_id)
        self.commit(query)
        return


# Creates an instance for the DBManager class for export.
dbManager = DBManager()
