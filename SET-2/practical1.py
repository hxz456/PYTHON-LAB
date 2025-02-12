class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"Withdrawn {amount}. New balance: {self.balance}")

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self.account = None

    def open_account(self, account_number, initial_deposit):
        self.account = Account(account_number, initial_deposit)
        print(f"Account {account_number} opened for {self.name} with balance {initial_deposit}")

class Bank:
    def __init__(self, name):
        self.name = name
        self.customers = []

    def add_customer(self, customer):
        self.customers.append(customer)
        print(f"Customer {customer.name} added to {self.name}")

# Example Usage
bank = Bank("ABC Bank")
customer = Customer("John Doe", 101)
bank.add_customer(customer)
customer.open_account(123456, 500)
customer.account.deposit(200)
customer.account.withdraw(100)
