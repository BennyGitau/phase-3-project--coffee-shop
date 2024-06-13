#!/usr/bin/env python3
# lib/debug.py

from models.coffee_order import Order
from models.customer import Customer
from models.comment import Comment
import ipdb

from models.customer import Customer
def reset_database():
    Order.drop_table()
    Order.create_table_orders()
    Customer.drop_table()
    Customer.create_table()
    Comment.drop_table()
    Comment.create_table()

    #seed data
    customer1 = Customer.create_user('Joan', 'Mpesa')
    customer2 = Customer.create_user('James', 'Visa')
    customer3 = Customer.create_user('Trizah', 'MasterCard')
    customer4 = Customer.create_user('Alice', 'Mpesa')
    customer5 = Customer.create_user('Bob', 'Visa')
    order1 = Order.create('Americano', customer1.id)
    order2 = Order.create('Latte', customer2.id)
    order = Order.create('Espresso', customer1.id)
    order3 = Order.create('Cappuccino', customer3.id)
    order4 = Order.create('Macchiato', customer4.id)
    order5 = Order.create('Mocha', customer5.id)
    order6 = Order.create("Ristretto", customer5.id)
    Comment.create('Trizah', 'Coffee is good but slow services and unprofessional staff', order.id)
    Comment.create('James', 'Sweet', order1.id)
    Comment.create('Trizah', 'my favorite', order2.id)
    Comment.create('Joan', 'awful', order3.id)
    Comment.create('Alice', 'perfect', order4.id)
    Comment.create('Bob', 'waste of money', order5.id)
    Comment.create('Bob', 'not as expected', order6.id)

reset_database()
ipdb.set_trace()
