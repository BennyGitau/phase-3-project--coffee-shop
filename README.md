# Coffee Shop Program

## Table of Contents

- [Introduction](#introduction)
- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Setup and Installation](#setup-and-installation)
- [Features and Usage](#features-and-usage)
  - [Customer Menu](#customer-menu)
  - [Admin Menu](#admin-menu)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Introduction

In the rapidly advancing world of business technology and performance-driven enterprises, leveraging customer reviews for performance rating and marketing is crucial. Coffee Shop is a program designed to manage small businesses such as cafes, ensuring that customers can input their feedback for ratings.

## Overview

Coffee Shop allows small businesses, especially cafes, to manage customer feedback and orders effectively. The program provides functionalities for both customers and administrators to streamline operations, improve customer satisfaction, and track business performance through sales and feedback.

## Prerequisites

Before you begin, ensure you have met the following requirements:
- You have Python installed on your machine (version 3.8 and above).
- You have a code editor installed, preferably VSCode.
- You have access to the internet to download dependencies.

## Setup and Installation

To set up and install the Coffee Shop program, follow these steps:

1. **Install Python**: Ensure Python 3.8 or above is installed on your machine. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Install VSCode**: Download and install [VSCode](https://code.visualstudio.com/).

3. **Fork and Clone the Repository**: 
    ```sh
    git clone https://github.com/BennyGitau/phase-3-project--coffee-shop.git
    ```

4. **Navigate to the Project Directory**:
    ```sh
    cd phase-3-project--coffee-shop
    ```

5. **Create a Virtual Environment and Install Dependencies**:
    ```sh
    pipenv install
    pipenv shell
    ```

6. **Run the Program**:
    - To start the program:
        ```sh
        ./lib/seed.py
        ./lib/cli.py
        ```

   If you encounter a "permission denied" error, run:
    ```sh
    chmod +x lib/seed.py
    chmod +x lib/cli.py
    ```

## Features and Usage

Coffee Shop provides two main interfaces: Customer and Admin.

### Customer Menu

- **Registration**: Register by entering your name and selecting a preferred method of payment to get a customer ID.
- **Update Payment Method**: Change your preferred method of payment.
- **Create Order**: Add a coffee order using your customer ID.
- **Create Comment**: Comment on the coffee or services received after placing an order.
- **Update Comment**: Update a comment using the comment ID.
- **Delete Comment**: Delete a comment using the comment ID.
- **Go Back**: Navigate to the main menu.
- **Exit**: Exit the program.

### Admin Menu

- **Find a Customer**: Search for a customer using their name or customer ID.
- **Delete a Customer**: Remove a customer from the database.
- **View All Customers**: Display a list of all customers.
- **Update a Customer Order**: Modify a customer’s order.
- **List All Orders**: Display all orders.
- **Find an Order**: Search for an order using customer ID or order ID.
- **Delete an Order**: Remove an order using order ID.
- **View Comments**: Display all comments or filter by positive, negative, or neutral.
- **Total Sales**: View total sales for a specific date.
- **Go Back**: Navigate to the main menu.
- **Exit**: Exit the program.

## Contributing

To contribute to the Coffee Shop project:

1. Fork the repository.
2. Create a new branch:
    ```sh
    git checkout -b feature/your-feature-name
    ```
3. Make your changes and commit them:
    ```sh
    git commit -m 'Add some feature'
    ```
4. Push to the branch:
    ```sh
    git push origin feature/your-feature-name
    ```
5. Create a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For any questions or contributions, please contact:

### Benson Gitau

[✉️ Email](mailto:bensonkamaugitau@gmail.com)

---

### ©️Coffee Shop



