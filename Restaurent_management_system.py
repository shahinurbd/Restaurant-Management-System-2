menu = {
    "Pizza": 12.99,
    "Burger": 8.99,
    "Pasta": 10.99,
    "Salad": 6.99,
    "Coffee": 3.99,
    "Juice": 4.99
}

class Customer:
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address
        self.balance = 0.0
        self.past_orders = []

    def view_menu(self, menu):
        print("\n--- Restaurant Menu ---")
        for item, price in menu.items():
            print(f"{item}: ${price:.2f}")

    def place_order(self, menu):
        print("\nEnter the items you want to order (type 'done' to finish):")
        order = {}
        while True:
            item = input("Item name: ").strip()
            if item.lower() == 'done':
                break
            if item not in menu:
                print("Item not available in menu. Please try again.")
                continue
            quantity = int(input(f"Enter quantity for {item}: ").strip())
            if quantity <= 0:
                print("Invalid quantity. Please enter a positive value.")
                continue
            order[item] = order.get(item, 0) + quantity
        total_cost = sum(menu[item] * quantity for item, quantity in order.items())
        if total_cost > self.balance:
            print(f"\nInsufficient balance! Your balance is ${self.balance:.2f}, but the total order cost is ${total_cost:.2f}.")
            return
        self.balance -= total_cost
        self.past_orders.append(order)
        print(f"\nOrder placed successfully! Your new balance is ${self.balance:.2f}")
        print("Ordered items:")
        for item, quantity in order.items():
            print(f"{item} x{quantity}")

    def view_past_orders(self):
        print("\n--- Past Orders ---")
        if not self.past_orders:
            print("No past orders found.")
            return

        for i, order in enumerate(self.past_orders, start=1):
            print(f"Order {i}:")
            for item, quantity in order.items():
                print(f"  {item} x{quantity}")

    def check_balance(self):
        print(f"\nYour available balance is: ${self.balance:.2f}")

    def add_funds(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Funds added successfully! New balance: ${self.balance:.2f}")
        else:
            print("Invalid amount. Please add a positive value.")

class Admin:
    def __init__(self):
        self.customers = []
        self.menu = {}

    def create_menu_item(self, item, price):
        if item in self.menu:
            print(f"{item} already exists in the menu.")
        else:
            self.menu[item] = price
            print(f"{item} added to the menu with price ${price:.2f}.")

    def remove_menu_item(self, item):
        if item in self.menu:
            del self.menu[item]
            print(f"{item} removed from the menu.")
        else:
            print(f"{item} does not exist in the menu.")

    def update_menu_item(self, item, price):
        if item in self.menu:
            self.menu[item] = price
            print(f"Price of {item} updated to ${price:.2f}.")
        else:
            print(f"{item} does not exist in the menu.")

    def add_customer(self, name, email, address):
        customer = Customer(name, email, address)
        self.customers.append(customer)
        print(f"Customer {name} added successfully.")

    def view_customers(self):
        print("\n--- Registered Customers ---")
        if not self.customers:
            print("No customers registered.")
        else:
            for i, customer in enumerate(self.customers, start=1):
                print(f"{i}. Name: {customer.name}, Email: {customer.email}, Address: {customer.address}")

    def remove_customer(self, email):
        for customer in self.customers:
            if customer.email == email:
                self.customers.remove(customer)
                print(f"Customer with email {email} removed successfully.")
                return
        print(f"Customer with email {email} not found.")


class Restaurant:
    def __init__(self):
        self.menu = {}
        self.customers = []

    def add_menu_item(self, item, price):
        if item in self.menu:
            print(f"{item} already exists in the menu.")
        else:
            self.menu[item] = price
            print(f"{item} added to the menu with price ${price:.2f}.")

    def remove_menu_item(self, item):
        if item in self.menu:
            del self.menu[item]
            print(f"{item} removed from the menu.")
        else:
            print(f"{item} does not exist in the menu.")

    def update_menu_item(self, item, price):
        if item in self.menu:
            self.menu[item] = price
            print(f"Price of {item} updated to ${price:.2f}.")
        else:
            print(f"{item} does not exist in the menu.")

    def view_menu(self):
        print("\n--- Restaurant Menu ---")
        if not self.menu:
            print("Menu is empty.")
        else:
            for item, price in self.menu.items():
                print(f"{item}: ${price:.2f}")

    def add_customer(self, name, email, address):
        customer = Customer(name, email, address)
        self.customers.append(customer)
        print(f"Customer {name} added successfully.")

    def view_customers(self):
        print("\n--- Registered Customers ---")
        if not self.customers:
            print("No customers registered.")
        else:
            for i, customer in enumerate(self.customers, start=1):
                print(f"{i}. Name: {customer.name}, Email: {customer.email}, Address: {customer.address}")

    def remove_customer(self, email):
        for customer in self.customers:
            if customer.email == email:
                self.customers.remove(customer)
                print(f"Customer with email {email} removed successfully.")
                return
        print(f"Customer with email {email} not found.")

def admin_menu():
    admin = Admin()
    while True:
        print('--- Admin Menu ---')
        print('1.Create Customer Account')
        print('2.Remove Customer Account')
        print('3.View All Customer')
        print('4.Manage Restaurent Menu')
        print('5.Exit')
        choice = int(input('Enter your choice: '))
        if choice == 1:
            name = input('Name: ')
            email = input('Email: ')
            address = input('Address: ')
            admin.add_customer(name=name,email=email,address=address)
        elif choice == 2:
            email = input('Email: ')
            admin.remove_customer(email=email)

        elif choice == 3:
            admin.view_customers()

        elif choice == 4:
            restaurent_menu()

        elif choice == 5:
            break

        else:
            print('Invalid choice, Try again!')

def customer_menu():
    name = input('Name: ')
    email = input('Email: ')
    address = input('Address: ')
    cus = Customer(name=name,email=email,address=address)
    while True:
        print(f"---- {name}'s Menu ----")
        print('1.View Restaurent Menu')
        print('2.View Balance')
        print('3.Add Balance')
        print('4.Place Order')
        print('5.View Past Orders')
        print('6.Exit')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            cus.view_menu(menu)

        elif choice == 2:
            cus.check_balance()

        elif choice == 3:
            amount = int(input('Enter balance amount: '))
            cus.add_funds(amount)

        elif choice == 4:
            cus.place_order(menu)

        elif choice == 5:
            cus.view_past_orders()

        elif choice == 6:
            break
        else:
            print('Invalid choice, Try again!')

def restaurent_menu():
    res = Restaurant() 
    while True:
        print('---- Restaurent Menu -----')
        print('1.Add Menu Item')      
        print('2.Remove Menu Item')      
        print('3.Update Menu Item')      
        print('4.View Menu Items')      
        print('5.Exit')
        choice = int(input('Enter your choice: '))

        if choice == 1:
            item_name = input('Item Name: ')
            price = int(input('Price: '))
            res.add_menu_item(item=item_name,price=price)

        elif choice == 2:
            item = input('Item Name: ')
            res.remove_menu_item(item=item)

        elif choice == 3:
            item_name = input('Item Name: ')
            price = int(input('Price: '))
            res.update_menu_item(item=item_name,price=price)

        elif choice == 4:
            res.view_menu()

        elif choice == 5:
            break
        else:
            price('Invalid choice,Try Again!')     

#Main page
while True:
    print('---- Restaurent Management System ----')
    print('1.Admin Login')
    print('2.Customer Login')
    print('3.Exit')
    choice = int(input('Select an option: '))

    if choice == 1:
        admin_menu()

    elif choice == 2:
        customer_menu()

    elif choice == 3:
        break
    else:
        print('Invalid choice,Try again!')







    


    

    
    




    