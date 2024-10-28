import mysql.connector
import uuid

class DatabaseManager:
    def __init__(self, host, user, password, db):
        self.con = mysql.connector.connect(host=host, user=user, password=password, database=db)
        if self.con.is_connected():
            print("Connected")
        else:
            print("Unable to connect")
        self.cur = self.con.cursor()
        self.create_tables()

    def create_tables(self):
        # Create necessary tables
        self.cur.execute("CREATE TABLE IF NOT EXISTS costumer(costumer_id VARCHAR(70) PRIMARY KEY, name VARCHAR(30), E_Mail VARCHAR(30), mobile VARCHAR(10), address VARCHAR(50));")
        self.cur.execute("CREATE TABLE IF NOT EXISTS main(company VARCHAR(10), model VARCHAR(10), colour VARCHAR(10), storage VARCHAR(3), screen_size VARCHAR(50), price VARCHAR(50), quantity VARCHAR(10));")
        self.con.commit()

    def check_product(self, model, colour, storage):
        try:
            self.cur.execute("SELECT * FROM main WHERE model=%s AND colour=%s AND storage=%s;", (model, colour, storage))
            return bool(self.cur.fetchall())
        except Exception as e:
            print("Error ", e)
            return False

    def check_customer(self, customer_id):
        try:
            self.cur.execute("SELECT * FROM costumer WHERE costumer_id=%s;", (customer_id,))
            return bool(self.cur.fetchall())
        except Exception as e:
            print("Error ", e)
            return False

    def add_product(self):
        print("|ADD PRODUCT|")
        company = input("ENTER COMPANY: ")
        model = input("ENTER MODEL NAME: ")
        colour = input("ENTER COLOUR: ")
        storage = input("ENTER STORAGE(Gb): ")
        screen_size = input("ENTER SCREEN SIZE: ")
        price = input("ENTER PRICE: ")

        if self.check_product(model, colour, storage):
            print("YOUR PRODUCT ALREADY EXISTS")
            self.cur.execute("SELECT quantity FROM main WHERE model=%s AND colour=%s AND storage=%s;", (model, colour, storage))
            stock_quantity = self.cur.fetchone()[0]
            print("NUMBER OF PRODUCTS ALREADY IN STOCK ", stock_quantity)
            new_quantity = int(input("ENTER THE QUANTITY TO BE ADDED")) + int(stock_quantity)
            self.cur.execute("UPDATE main SET quantity=%s WHERE model=%s AND colour=%s AND storage=%s;", (new_quantity, model, colour, storage))
            print("Updated")
        else:
            quantity = input("ENTER QUANTITY: ")
            self.cur.execute("INSERT INTO main (company, model, colour, storage, screen_size, price, quantity) VALUES (%s, %s, %s, %s, %s, %s, %s);", 
                             (company, model, colour, storage, screen_size, price, quantity))
            print("Record Added")
        self.con.commit()

    def remove_product(self):
        print("|REMOVE PRODUCT|")
        model = input("Enter Model: ")
        colour = input("Enter Colour: ")
        storage = input("Enter Storage: ")
        
        if self.check_product(model, colour, storage):
            self.cur.execute("SELECT quantity FROM main WHERE model=%s AND colour=%s AND storage=%s;", (model, colour, storage))
            stock_quantity = int(self.cur.fetchone()[0])
            quantity_to_remove = int(input("ENTER QUANTITY TO REMOVE: "))
            
            if quantity_to_remove >= stock_quantity:
                self.cur.execute("DELETE FROM main WHERE model=%s AND colour=%s AND storage=%s;", (model, colour, storage))
                print("Product Removed")
            else:
                new_quantity = stock_quantity - quantity_to_remove
                self.cur.execute("UPDATE main SET quantity=%s WHERE model=%s AND colour=%s AND storage=%s;", (new_quantity, model, colour, storage))
                print("Updated")
        else:
            print("Product not found")
        self.con.commit()

    def display_stock(self):
        print("|STOCK|")
        self.cur.execute("SELECT * FROM main;")
        for record in self.cur.fetchall():
            print(record)

    def product_details(self):
        company = input("ENTER COMPANY: ")
        model = input("ENTER MODEL: ")
        storage = input("ENTER STORAGE: ")
        self.cur.execute("SELECT * FROM main WHERE company=%s AND model=%s AND storage=%s;", (company, model, storage))
        for record in self.cur.fetchall():
            print(record)

    def add_customer(self):
        customer_id = str(uuid.uuid4())
        print("Customer's unique ID:", customer_id)
        name = input("ENTER NAME: ")
        email = input("E-MAIL: ")
        mobile = input("ENTER MOBILE NUMBER: ")
        address = input("ENTER ADDRESS: ")
        self.cur.execute("INSERT INTO costumer (costumer_id, name, E_Mail, mobile, address) VALUES (%s, %s, %s, %s, %s);", 
                         (customer_id, name, email, mobile, address))
        print("Customer Record Added")
        self.con.commit()

    def remove_customer(self):
        customer_id = input("Enter Customer ID: ")
        if self.check_customer(customer_id):
            self.cur.execute("DELETE FROM costumer WHERE costumer_id=%s;", (customer_id,))
            print("Customer Deleted")
        else:
            print("Customer not found")
        self.con.commit()

    def update_customer(self):
        customer_id = input("Enter Customer ID: ")
        if not self.check_customer(customer_id):
            print("Customer not found")
            return

        print("Select the information to update:")
        options = {
            1: ("name", "Enter new name: "),
            2: ("E_Mail", "Enter new email: "),
            3: ("mobile", "Enter new mobile number: "),
            4: ("address", "Enter new address: ")
        }
        while True:
            for key, value in options.items():
                print(f"{key}. {value[0].capitalize()}")
            choice = int(input("Select an option or 5 to exit: "))
            if choice == 5:
                break
            elif choice in options:
                new_value = input(options[choice][1])
                self.cur.execute(f"UPDATE costumer SET {options[choice][0]}=%s WHERE costumer_id=%s;", (new_value, customer_id))
                print("Customer information updated")
            else:
                print("Invalid option")
        self.con.commit()

    def display_customer_database(self):
        self.cur.execute("SELECT * FROM costumer;")
        for record in self.cur.fetchall():
            print(record)

    def customer_details(self):
        customer_id = input("Enter Customer ID: ")
        self.cur.execute("SELECT * FROM costumer WHERE costumer_id=%s;", (customer_id,))
        for record in self.cur.fetchall():
            print(record)

    def close_connection(self):
        self.cur.close()
        self.con.close()
        print("Connection closed")
        
# Usage Example
# Call appropriate methods to perform actions, e.g.:
# db_manager.add_product()
# db_manager.remove_product()
# db_manager.display_stock()
# db_manager.close_connection()
