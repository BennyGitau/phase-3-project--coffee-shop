from models.__init__ import CONN, CURSOR
from datetime import date

class Customer:
    all= {}  # dictionary to store all customers

    def __init__(self, name, payment_method, date=None, id =None):
        """
        Initialize a new customer instance.

        Args:
            name (str): The name of the customer.
            payment_method (str): The payment method of the customer.
            date (datetime): The date the customer visited.
            id (int): The unique id of the customer.
        """
        self.name = name
        self.date = date
        self.id = id
        self.payment_method = payment_method
        type(self).all[self.id] = self

    def __repr__(self):
        """
        Return string representation of the customer object.

        Returns:
            str: The string representation of the customer object.
        """
        return f'<ID {self.id}: {self.name} visisted on {self.date}, and payed with {self.payment_method}>'
    
    @property
    def name(self):
        """
        Get the name of the customer.

        Returns:
            str: The name of the customer.
        """
        return self._name
    
    @name.setter
    def name(self, name):
        """
        Set the name of the customer.

        Args:
            name (str): The new name of the customer.
        """
        if not isinstance(name, str) or not len(name) >0:
            raise ValueError('Name must be a non-empty string')
        self._name = name
    @property
    def payment_method(self):
        """
        Get the payment method of the customer.

        Returns:
            str: The payment method of the customer.
        """
        return self._payment_method
    @payment_method.setter
    def payment_method(self, value):
        """
        Set the payment method of the customer.

        Args:
            value (str): The new payment method of the customer.
        """
        if not isinstance(value, str) or not len(value) > 0:
            raise ValueError('payment_method must be a non-empty string')
        self._payment_method = value
    
    @classmethod
    def create_table(cls):
        """
        Create the customers table in the database if it does not exist.
        """
        CURSOR.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                id INTEGER PRIMARY KEY,
                name TEXT UNIQUE NOT NULL,
                payment_method TEXT NOT NULL,
                date_visited DATE DEFAULT (DATE('now', 'localtime'))
            )
        ''')
        #date_visited DATE DEFAULT (DATE('now', 'localtime'))
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """
        Drop the customers table from the database.
        """
        CURSOR.execute('''DROP TABLE IF EXISTS customers''')
        CONN.commit()

    def save(self):
        """
        Save the customer to the database.
        """
        date_visited = date.today()
        CURSOR.execute('''INSERT INTO customers (name, payment_method) VALUES (?,?)''',
                           (self.name, self.payment_method))
        self.id = CURSOR.lastrowid
        self.date = date_visited
        CONN.commit()
        type(self).all[self.id] = self

    @classmethod
    def create_user(cls, name, payment_method):
        """
        Create a new customer and save it to the database.

        Args:
            name (str): The name of the customer.
            payment_method (str): The payment method of the customer.

        Returns:
            Customer: The newly created customer.
        """
        #initializes a new user
        user = cls(name, payment_method)
        user.save()
        return user

    def update(self):
        """
        Update the payment method of the customer in the database.
        """
        #update a specific user
        CURSOR.execute('''UPDATE customers SET payment_method=? WHERE id=?''',
                       (self.payment_method, self.id))
        CONN.commit()

    def delete(self):
        """
        Delete the customer from the database.
        """
        #delete a specific user
        CURSOR.execute('''DELETE FROM customers WHERE id=?''', (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None
 
    @classmethod
    def instance_from_db(cls, row):
        """
        Create a Customer instance from a row in the database.

        Args:
            row (tuple): The row from the database.

        Returns:
            Customer: The Customer instance created from the row.
        """
        #check if a user exists in the dictionary
        customer = cls.all.get(row[0])
        if customer:
            #match the user attributes with row values
            customer.name = row[1]
            customer.payement_method = row[2]
            customer.date = row[3]
        else:
            #if user is not found create a new one
            customer = cls(row[1], row[2], row[3])
            customer.id = row[0]
            cls.all[customer.id] = customer
        return customer

    @classmethod
    def get_all(cls):
        """
        Get all customers from the database.

        Returns:
            list: A list of Customer instances.
        """
        #Returns all users in users table
        CURSOR.execute('''SELECT * FROM customers''')
        return [cls.instance_from_db(row) for row in CURSOR.fetchall()]

    @classmethod
    def get_by_id(cls, id):
        """
        Get a customer from the database by their id.

        Args:
            id (int): The id of the customer.

        Returns:
            Customer: The Customer instance with the given id.
        """
        sql = '''SELECT * FROM customers WHERE id = ?'''
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def get_by_username(cls, name):
        """
        Get a customer from the database by their name.

        Args:
            name (str): The name of the customer.

        Returns:
            Customer: The Customer instance with the given name.
        """
        sql = '''SELECT * FROM customers WHERE name = ?'''
        row = CURSOR.execute(sql, (name,)).fetchone()

        return cls.instance_from_db(row) if row else None
    
    def customers(self):
        """
        Get all orders associated with the customer.

        Returns:
            list: A list of Order instances.
        """
        from models.coffee_order import Order
        #returns a list of users associated with a post
        sql = '''SELECT * FROM customers WHERE customer_id = ?'''
        rows = CURSOR.execute(sql, (self.id,)).fetchall()
        return [Order.instance_from_db(row) for row in rows]


