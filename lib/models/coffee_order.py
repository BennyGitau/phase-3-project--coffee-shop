from models.customer import Customer
from models.__init__ import CONN, CURSOR
class Order:
    all = {}
    def __init__(self, order_item, customer_id, price=10, id=None):
        self.id = id
        self.order_item = order_item
        self.price = price
        self._customer_id = customer_id
        type(self).all[self.id] = self

    def __repr__(self):
        return f'<Order {self.id}: {self._order_item}, price: ${self.price}  >'

    @property
    def order_item(self):
        return self._order_item
    
    @order_item.setter
    def order_item(self, item):
        if not isinstance(item, str) or not len(item):
            raise ValueError('Content must be a non-empty string')
        self._order_item = item

    @property
    def customer_id(self):
        return self._customer_id
    
    @customer_id.setter
    def customer_id(self, value):
        if not type(value) is int or not Customer.get_by_id(value):
            raise ValueError('Customer is not valid')
        self._customer_id = value

    @classmethod
    def create_table_orders(cls):
        # Create orders table
        CONN.execute('''
            CREATE TABLE IF NOT EXISTS orders (
                id INTEGER PRIMARY KEY,
                order_item TEXT,
                price INTEGER CHECK(price BETWEEN 10 AND 20),
                customer_id INTEGER,
                FOREIGN KEY (customer_id) REFERENCES customers(id)
            )
        ''')

        # Create trigger to set a random price when inserting a new row
        CONN.execute('''
            CREATE TRIGGER IF NOT EXISTS set_price_above_10
            BEFORE INSERT ON orders
            FOR EACH ROW
            BEGIN
                UPDATE orders SET price = 10 + (random() * 10) WHERE NEW.price IS NULL;
            END;
        ''')

        CONN.commit()

    @classmethod
    def drop_table(cls):
        CURSOR.execute(""" DROP TABLE IF EXISTS orders""")
        CONN.commit()

    def save(self):
        import random
        price = 10 + int(random.random() * 10)
        CURSOR.execute("""
                INSERT INTO orders (order_item, price, customer_id) VALUES (?,?,?)
        """, (self.order_item, price, self.customer_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, order_item, customer_id):
        order = cls(order_item, customer_id)
        order.save()
        return order
    
    def update(self):
        CURSOR.execute('''UPDATE orders SET order_item = ? WHERE id = ?''', (self.order_item, self.id))
        CONN.commit()
    
    def delete(self):
        CURSOR.execute("""DELETE FROM orders WHERE id = ? """, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        order = cls.all.get(row[0])
        if order:
            order.order_item = row[1]
            order.price = row[2]
            order.customer_id = row[3]
        else:
            order = cls(row[1], row[2], row[3])
            order.id = row[0]
            cls.all[order.id] = order
        return order
    
    @classmethod
    def get_all(cls):
        sql = '''SELECT * FROM orders'''
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    @classmethod
    def get_by_id(cls, id):
        sql = '''SELECT * FROM orders WHERE id = ?'''
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def get_by_customer_id(cls, customer_id):
        sql = '''SELECT * FROM orders WHERE customer_id = ?'''
        row = CURSOR.execute(sql, (customer_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    @classmethod
    def orders(cls, customer_id):
        #return a list of posts associated with a user
        sql = '''SELECT * FROM posts WHERE user_id = ?'''
        rows = CURSOR.execute(sql, (customer_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]
    @classmethod
    def total_sales(cls, date):
        
        #return a total sales of certain day
        sql = '''
                SELECT orders.price
                FROM orders
                INNER JOIN customers ON orders.customer_id = customers.id
                WHERE customers.date_visited = ?
                '''
        
        sales= CONN.execute(sql, (date,)).fetchall()
        totalsales = sum(sale[0] for sale in sales)

        return totalsales
    