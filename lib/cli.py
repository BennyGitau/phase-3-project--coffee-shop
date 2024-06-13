#!/usr/bin/env python3
# lib/cli.py

import fire
from models.__init__ import CONN,CURSOR
from helpers import (
    exit_program,
    clear,
    list_users,
    find_customer_by_username,
    find_customer_by_id,
    delete_customer,
    update_customer,
    create_customer,
    list_comments,
    delete_comment,
    update_comment,
    create_comment,
    create_order,
    list_orders,
    update_order,
    delete_order,
    find_order_by_id,
    find_order_by_customer_id,
    total_sales
    
)


def help():
    print("--admin--      -- to navigate as admin")
    print("--customer--   -- to navigate as customer")
    print("--clear--      -- to clear screen")
    print("--exit--       -- to exit program")

def navigation():
    while True:
        print('===========================================NAVIGATION==================================================')
        print("                                           --Admin--")
        print("                                           --Customer--")
        print("                                           --help--")
        print("                                           --exit--")
        print("-------------------------------------------------------------------------------------------------------")

        choice = input("Enter option> ").strip().lower()
        if choice == "admin":
                admin()
        elif choice == "customer":
                customer()
        elif choice == "exit":
                exit_program()
        elif choice == "clear":
                clear()
        elif choice == "help":
                help()
        else:
            print("Invalid option")


def customer():
    CONN.execute("""PRAGMA foreign_keys = ON""")

    while True:
        print("===========================================OPTIONs=====================================================")
        print("                                       --1 --Register")
        print("                                       --2 --Update payment method")
        print("                                       --3 --Create order")
        print("                                       --4 --Create comment")
        print("                                       --5 --Update comment")
        print("                                       --6 --Delete comment")
        print("                                       --0 --Go back")
        print("                                       --00 --Exit")
   
        choice = input("Enter option: ").strip()
        if choice == "0":
            break
        elif choice == "00":
            exit_program()
        elif choice == "1":
            create_customer()
        elif choice == "2":
            update_customer()
        elif choice == "3":
            create_order()
        elif choice == "4":
            create_comment()
        elif choice == "5":
            update_comment()
        elif choice == "6":
            delete_comment()
        elif choice == "clear":
            clear()
        else:
            print("Invalid option")
def admin():
    while True:
        print("========================================OPTIONs=======================================================")
        print("                                     --1 --Find customer by id")
        print("                                     --2 --Find customer by name")
        print("                                     --3 --Delete customer")
        print("                                     --4 --List customers")
    
        print("                                     --5 --Update order")
        print("                                     --6 --List orders")
        print("                                     --7 --Find order by id")
        print("                                     --8 --Find order by customer_id")
        print("                                     --9 --Delete order")

        print("                                     --10 --view comments")
        print("                                     --11 --Total sales")
        print("                                     --0  --go back")
        print("                                     --00 --exit")
        
        choice = input("Select option: ")
        if choice == "0":
            break
        elif choice == "00":
            exit_program()
        elif choice == "1":
            find_customer_by_id()
        elif choice == "2":
            find_customer_by_username()
        elif choice == "3":
            delete_customer()
        elif choice == "4":
            list_users()
        elif choice == "5":
            update_order()
        elif choice == "6":
            list_orders()
        elif choice == "7":
            find_order_by_id()
        elif choice == "8":
            find_order_by_customer_id()
        elif choice == "9":
            delete_order()
        elif choice == "10":
            list_comments()
        elif choice == "11":
            total_sales()
        elif choice == "clear":
            clear()
        else:
            print("Invalid option")

def main():
    while True:
        navigation()


if __name__ == "__main__":
    fire.Fire(main())
