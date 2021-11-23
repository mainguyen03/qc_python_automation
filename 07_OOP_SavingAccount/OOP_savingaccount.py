from datetime import datetime

class Customer:
    def __init__(self, name, date_of_birth, email, phone):
        self.name = name
        self.date_of_birth = datetime.strptime(date_of_birth, "%d/%m/%Y").date()
        self.email = email
        self.phone = phone

    def get_info(self):
        print("Customer name:", self.name)
        print("Date of birth:", self.date_of_birth)
        print("Email:", self.email)
        print("Phone:", self.phone)

# Use Property
class BankAccount():
    def __init__(self, account_number, account_name, owner, balance = 0):
        self._account_number = account_number
        self._account_name = account_name
        self._owner = owner
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def owner(self):
        return self._owner

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount - self._balance >= 0 :
            self._balance = amount - self._balance
        else:
            print("Invalid number")

    def get_display(self):
        print("Account info")
        print("Account number:", self.account_number)
        self.owner.get_info()
        print("Balance:", self.balance, "₫")

    def set_withdraw(self, amount):
        if 0 < amount < self.get_balance(): 
            new_amount = self.get_balance() - amount
            self.set_balance(new_amount)
            print (f"withdraw {amount} $ from balance")
        else: 
            print ('Invalid Withdraw Amount')

    def set_deposit(self, amount):
        if amount > 0: 
            new_amount = self.get_balance() + amount
            self.set_balance(new_amount)
            print (f"Deposit {amount} $ to balance")
        else:
            print ('Invalid Deposit Amount')

class SavingAccount(BankAccount):
    monthly_interest_rate = 0.01

    def calculate_interest(self):
        return self._balance * self.monthly_interest_rate

Sao_Mai = Customer("Sao Mai", "10/10/2000", "saomai@gmail.com", "09xx")   

My_tech_acc = SavingAccount("190320xxxx", 'Sao Mai', Sao_Mai, 20)
My_tech_acc.get_display()
print(My_tech_acc.calculate_interest())
