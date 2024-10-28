# Product and Customer Management System

**Demo at - https://youtu.be/3qYwhNSWVCM**

## Project Overview

This project is a **Product and Customer Management System** built using Python and MySQL. It enables users to manage product inventory and customer records within a MySQL database. Using **Object-Oriented Programming (OOP)**, the project organizes database interactions into a class, making the code modular, reusable, and easy to maintain.

The project is designed with the following key functionalities:
- Adding, removing, and updating products in stock.
- Managing customer records, including adding, removing, and updating customer details.
- Displaying inventory and customer information with detailed views.

The `DatabaseManager` class handles all database interactions, providing a user-friendly interface to manage products and customers efficiently.

## Object-Oriented Programming (OOP) in the Project

The project applies **OOP principles** to improve code organization and structure:

1. **Encapsulation**: The `DatabaseManager` class encapsulates all the methods required for product and customer management. This design ensures that database interaction is contained within the class, making it easier to manage and modify.

2. **Modularity**: Each action (e.g., adding a product, removing a customer) is implemented as a separate method within the `DatabaseManager` class, making the code modular. These methods can be used independently, providing flexibility in code usage.

3. **Reusability**: By organizing database operations into methods, we can reuse code without duplication. For example, the same class can be extended or modified for additional functionalities without rewriting database connection logic.

4. **Simplicity**: The `DatabaseManager` class simplifies complex operations (like SQL queries) through easy-to-use methods. Users can perform operations without directly handling SQL queries, minimizing errors and enhancing ease of use.

## Features of the System

- **Product Management**:
  - Add new products or update existing product quantities.
  - Remove products or adjust stock levels based on availability.
  - Display and search products with detailed specifications.

- **Customer Management**:
  - Add, remove, or update customer records.
  - Display all customer records in the database.
  - Retrieve specific customer details for easy management.

## How to Use

1. **Initialize** the `DatabaseManager` object with your database credentials.
2. **Call methods** like `add_product()`, `remove_customer()`, etc., to perform various actions.
3. **Close the connection** using `close_connection()` when all operations are complete.

This structured, OOP-based project is a scalable and efficient solution for managing product inventories and customer information within a MySQL database.



# Mobile Showroom Management System -Methods Overview

## 1. Product Management Methods

- **`add_product()`**
  - Prompts for product details and adds the product to the database. If the product already exists, it updates the quantity.

- **`remove_product()`**
  - Prompts for the model, color, and storage of a product to remove or decrease the quantity. If the quantity is zero, the product is deleted.

- **`display_stock()`**
  - Displays a list of all products in the database, showing details like company, model, color, storage, screen size, and price.

- **`product_details()`**
  - Prompts for the company, model, and storage of a product to retrieve and display detailed information about it.

## 2. Customer Management Methods

- **`add_customer()`**
  - Prompts for customer details (name, email, mobile, address) and adds a new customer to the database with a unique ID.

- **`remove_customer()`**
  - Prompts for a customer's unique ID to remove that customer from the database.

- **`update_customer()`**
  - Prompts for a customer's ID and allows updating specific details (name, email, mobile number, or address).

- **`display_customer_database()`**
  - Displays all customer records in the database with their details.

- **`customer_details()`**
  - Prompts for a customer’s ID and retrieves detailed information about that specific customer.

## 3. Database Connection Method

- **`close_connection()`**
  - Closes the connection to the database when all operations are complete.
