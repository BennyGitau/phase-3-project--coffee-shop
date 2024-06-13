from models.__init__ import CONN, CURSOR

class Comment:
    all ={}

    # Initialize a new Comment object
    def __init__(self, username, content, order_id=None, id=None):
        self.id = id
        self.username = username
        self.content = content
        self.order_id = order_id
        type(self).all[self.id] = self

    # Return a string representation of the Comment object
    def __repr__(self):
        return f'<Comment: {self.username} says {self.content} >'  

    # Getter and setter for the username property
    @property
    def username(self):
        return self._username
    
    @username.setter
    def username(self, username):
        from models.customer import Customer
        if not isinstance(username, str) or not Customer.get_by_username(username):
            raise ValueError('Customer is not valid')
        self._username = username

    # Getter and setter for the content property
    @property
    def content(self):
        return self._content
    
    @content.setter
    def content(self, content):
        if not isinstance(content, str) or not len(content):
            raise ValueError('Content must be a non-empty string')
        self._content = content

    # Getter and setter for the order_id property
    @property
    def order_id(self):
        return self._order_id
    
    @order_id.setter
    def order_id(self, order_id):
        from models.coffee_order import Order
        if not type(order_id) is int or not Order.get_by_id(order_id):
            raise ValueError('Order is not valid')
        self._order_id = order_id

    # Create the comments table in the database
    @classmethod
    def create_table(cls):
        CURSOR.execute('''
                    CREATE TABLE IF NOT EXISTS comments (
                    id INTEGER PRIMARY KEY,
                    username TEXT,
                    content TEXT,
                    order_id INTEGER,
                    FOREIGN KEY(order_id) REFERENCES orders(id),
                    FOREIGN KEY(username) REFERENCES customers(name)      
                    )
                    ''')
        CONN.commit()

    # Drop the comments table from the database
    @classmethod
    def drop_table(cls):
        CURSOR.execute(""" DROP TABLE IF EXISTS comments""")
        CONN.commit()

    # Save the Comment object to the database
    def save(self):
        CURSOR.execute("""
            INSERT INTO comments (username, content, order_id) VALUES (?,?,?)
        """, (self.username, self.content, self.order_id))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    # Create a new Comment object and save it to the database
    @classmethod
    def create(cls, username, content, order_id):
        comment = cls(username, content, order_id)
        comment.save()
        return comment

    # Update the content of a Comment object in the database
    def update_comment(self):
        CURSOR.execute('UPDATE comments SET content = ? WHERE id = ?', (self.content, self.id))
        CONN.commit()

    # Delete a Comment object from the database
    def delete_comment(self, id):
        CURSOR.execute('DELETE FROM comments WHERE id = ?', (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    # Create a Comment object from a database row
    @classmethod
    def instance_from_db(cls, row):
        comment = cls.all.get(row[0])
        if comment:
            comment.username = row[1]
            comment.content = row[2]
            comment.order_id = row[3]
        else:
            comment = cls(row[1], row[2], row[3])
            comment.id = row[0]
            cls.all[comment.id] = comment
        return comment

    # Get all Comment objects from the database
    @classmethod
    def get_all(cls):
        rows = CURSOR.execute('SELECT * FROM comments')
        return [cls.instance_from_db(row) for row in rows]
    
    # Get a Comment object from the database by id
    @classmethod
    def get_by_id(cls, id):
        row = CURSOR.execute('SELECT * FROM comments WHERE id = ?', (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    # Get a Comment object from the database by username
    @classmethod
    def get_by_username(cls, username):
        row = CURSOR.execute('SELECT * FROM comments WHERE username = ?', (username,)).fetchone()
        return cls.instance_from_db(row) if row else None

    # Get all Comment objects from the database by order_id
    @classmethod
    def find_by_order_id(cls, order_id):
        rows =CURSOR.execute('SELECT * FROM comments WHERE order_id = ?', (order_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    # Get all content fields from the comments table in the database
    @classmethod
    def reviews(cls):
        reviews = CURSOR.execute('SELECT content FROM comments').fetchall()
        return [review[0] for review in reviews]


