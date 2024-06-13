# lib/helpers.py
from models.customer import Customer
from models.coffee_order import Order
from models.comment import Comment
import re


def exit_program():
    print(f"Thank you for using our program 😙. Goodbye!")
    exit()

def clear():
    import os
    print("cleared")
    os.system("cls" if os.name == "nt" else "clear")

# Helper functions for order class
def create_order():
    coffee = input("Enter coffee cup: ").strip().capitalize()
    customer_id_ = input("Enter customer_id: ").strip()
    if not customer_id_.isdigit():
        print("invalid customer_id")
        return
    if coffee.isdigit():
        print("invalid coffee cup")
        return
    
    try:
        order = Order.create(coffee, int(customer_id_))
        print(f"Order created: {order}")
    except Exception:
        print(f"Error creating order: customer {customer_id_} not found")

def update_order():
    id = input("Enter id: ").strip()
    if not id.isdigit():
        print("ID must be an integer.")
        return
    if order := Order.get_by_id(int(id)):
        try:
            coffee = input("Enter coffee cup: ").strip().capitalize()
            if coffee.isdigit():
                print("invalid coffee cup")
                return
            order.order_item = coffee
            order.update()
            print(f"Order updated: {order}")
        except Exception as e:
            print(f"Error: Order {id} not found")
    else:
        print(f"Order with ID {id} not found.")

def delete_order():
    id = input("Enter id: ").strip()
    if not id.isdigit():
        print("ID must be an integer.")
        return
    order = Order.get_by_id(int(id))
    if order:
        order.delete()
        print(f"{id} deleted.")
    else:
        print(f"Order with ID {id} not found.")

def find_order_by_id():
    id = input("Enter id: ").strip()
    if not id.isdigit():
        print("ID must be an integer.")
        return
    order = Order.get_by_id(int(id))
    print(order) if order else print(f'Order with ID {id} not found.')

def find_order_by_customer_id():
    customer_id = input("Enter customer_id: ").strip()
    if not customer_id.isdigit():
        print("Customer ID must be an integer.")
        return
    order = Order.get_by_customer_id(int(customer_id))
    print(order) if order else print(f'Orders for customer ID {customer_id} not found.')

def list_orders():
    orders = Order.get_all()
    for order in orders:
        print(order)

# Helper functions for comment class
def create_comment():
    username = input("Enter username: ").strip().capitalize()
    content = input("Enter comment: ").strip().capitalize()
    order_id = input("Enter order_id: ").strip()
    if not order_id.isdigit():
        print("Order ID must be an integer.")
        return
    if content.isdigit():
        print("Comment must be a string.")
        return
    if username.isdigit():
        print("Username must be a string.")
        return
    try:
        comment = Comment.create(username, content, int(order_id))
        print(f"Comment created: {comment}")
    except Exception:
        print(f"Error creating comment: Order {order_id} not found")

def update_comment():
    id = input("Enter id: ").strip()
    if not id.isdigit():
        print("ID must be an integer.")
        return
    if comment := Comment.get_by_id(int(id)):
        try:
            content = input("Enter comment: ").strip().capitalize()
            if content.isdigit() or not len(content):
                print("Comment must be a string.")
                return  
            comment.content = content
            comment.update_comment()
            print(f"Comment updated: {comment}")
        except Exception:
            print(f"Error updating comment: Comment {id} not found")
    else:
        print(f"Comment with ID {id} not found.")

def delete_comment():
    id_ = input("Enter id: ").strip()
    if not id_.isdigit():
        print("ID must be an integer.")
        return
    if comment := Comment.get_by_id(id_):
        try:
            comment.delete_comment(id_)
            print(f"Comment with ID {id_} deleted.")
        except Exception:
            print(f"Error deleting comment {id} not found")
    else:
        print(f"Comment with ID {id_} not found.")

def list_comments():
    reviews = Comment.reviews()
    positive_keywords = ['great', 'sweet', 'love', 'excellent', 'fast','perfect','worth','happy', 'favorite','quick','good','amazing','well','enjoyed']
    negative_keywords = [
                    'poor', 'not recommend', 'disappointing', 'slow','horrible','terrible', 'awful', 'bad', 'dreadful', 'rude', 'unprofessional', 
                    'inefficient', 'low-quality', 'nightmare', 'frustrating', 'overpriced', 'disgusted', 'regret', 'waste'
                    ]

    def preprocess(review):
        review = review.lower()
        review = re.sub(r'[^\w\s]', '', review)
        return review.split()

    def classify_review(review):
        tokens = preprocess(review)
        positive_count = sum(token in positive_keywords for token in tokens)
        negative_count = sum(token in negative_keywords for token in tokens)
        if positive_count > negative_count:
            return 'Positive'
        elif negative_count > positive_count:
            return 'Negative'
        else:
            return 'Neutral'

    classified_reviews = {
        "Positive": [],
        "Negative": [],
        "Neutral": []
    }

    for review in reviews:
        classification = classify_review(review)
        classified_reviews[classification].append(review)

    while True:
        print("===========================================OPTIONs=====================================================")
        print("                                       --A --View all reviews")
        print("                                       --P --View positive reviews")
        print("                                       --N --View negative reviews")
        print("                                       --F --View neutral reviews")
        print("                                       --0 --Go back")
        choice = input('Enter option: ').strip().upper()
        if choice == 'A':
            print("All Reviews:")
            for review in reviews:
                print(f"- {review}")
        elif choice == 'P':
            print("Positive Reviews:")
            for review in classified_reviews['Positive']:
                print(f"- {review}")
        elif choice == 'N':
            print("Negative Reviews:")
            for review in classified_reviews['Negative']:
                print(f"- {review}")
        elif choice == 'F':
            print("Neutral Reviews:")
            for review in classified_reviews['Neutral']:
                print(f"- {review}")
        elif choice == 'CLEAR':
            clear()
        elif choice == '0':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter A, P, N, F or 0.")

# Helper functions for customer class
def create_customer():
    name = input("Enter username: ").strip().capitalize()
    payment_method = input("Enter payment method: ").strip().capitalize()
    if  name.isdigit():
        print("Name must be a string.")
        return  
    if payment_method.isdigit():
        print("payment_method must be a string.")
        return   
    try:
        user = Customer.create_user(name, payment_method)
        print(f"User created: {user}")
    except Exception:
        print(f"Error creating user")

def update_customer():
    id = input("Enter id: ").strip()
    if not id.isdigit():
        print("ID must be an integer.")
        return
    if customer := Customer.get_by_id(int(id)):
        try:
            payment_method = input("Enter payment method: ").strip().capitalize()
            if payment_method.isdigit():
                print("Enter a valid payment method")
                return
            
            customer.payment_method = payment_method
            customer.update()
            print(f"User updated: {customer}")
        except Exception:
            print(f"Error updating customer: customer {id} not found")
    else:
        print(f"Customer with ID {id} not found")

def delete_customer():
    id_ = input("Enter id: ").strip()
    if not id_.isdigit():
        print("ID must be an integer.")
        return
    if customer := Customer.get_by_id(int(id_)):
        try:
            customer.delete()
            print(f"Customer {customer.name} deleted")
        except Exception:
            print(f"Error deleting customer: {id_} not found")
    else:
        print(f"Customer with ID {id_} not found")

def find_customer_by_id():
    id = input("Enter id: ").strip()
    if not id.isdigit():
        print("ID must be an integer.")
        return
    user = Customer.get_by_id(int(id))
    print(user) if user else print(f'Customer with ID {id} not found.')

def find_customer_by_username():
    name = input("Enter username: ").strip().capitalize()
    if name.isdigit():
        print("Name must be a string.")
        return
    user = Customer.get_by_username(name)
    if user:
        try:
            print(user)
        except Exception as e:
            print(f"Error: {name} not found")
    else:
        print(f"Customer with username {name} not found")

def list_users():
    users = Customer.get_all()
    for user in users:
        print(user)

def total_sales():
    date = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        sales = Order.total_sales(date)
        print(f"Total sales on {date}: ${float(sales):.2f}")
    except Exception:
        print(f"Error calculating total sales")
