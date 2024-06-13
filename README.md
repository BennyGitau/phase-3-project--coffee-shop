# Coffee shop
---


## Introduction

In the rapidly advancing world of business technology and performance-driven enterprises, leveraging customer reviews for performance rating and marketing is crucial. Coffee Shop is a program designed to manage small businesses such as cafes, ensuring that customers can input their feedback for ratings.

## setup and installation
To use the program;
- Ensure you have python installed in your machine --version 3.8 and above.
- Download and install Vscode editor
- Fork and clone this repository [<github repository>](https://github.com/BennyGitau/phase-3-project--coffee-shop)
- Open the repository in your termina and create a virtual environment
    ```console
    pipenv install
    pipenv shell
    ```
- Run the program
    ```console
    #to start with sample data run
    ./lib/seed.py
    # to start with an empty database
    ./lib/cli.py
     ```
     If you get an error --permission denied--
    ```console
    #run
    chmod +x lib/seed.py
    chmod +x lib/cli.py
    ```
## Features and usage
Coffee shop has two menus;
- Customer 
- Admin
    ### Customer
    -  Registration - customer registers by entering their name and selecting their preferred method of payment and get a customer ID
    -  Update payment method - customer can change their preferred method of payment
    -  Create order - a customer is able to add a cup of coffee they want by using their customer ID
    -  Create comment - after a customer an order, they can comment on the coffee or the services received
    -  Update comment - customer can update a comment using the comment ID received while creating the comment
    -  Delete comment - delete comment using the comment ID
    -  Go back - Navigate to main menu
    -  Exit - exit the program
    ### Admin
    - Find a customer using their name of customer ID
    - Delete a customer in the database
    - View a list of all customers
    - Update a customer order if they change their mind
    - List all the orders
    - Find an order using customer ID or order ID
    - Delete an order using order ID
    - View comments all, positive, negative, neutral
    - See total sales of a certain date
    - Go back to main menu
    - Exit program


## Contributions
Any one who would like to contribute to contact

[Benson](mailto:bensonkamaugitau@gmail.com)
---
### @Coffee shop



