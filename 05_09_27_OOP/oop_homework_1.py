class BankAccount():
    def __init__(self, account_number, account_name, balance = 1_000_000_000):
        self._account_number = account_number
        self._account_name = account_name
        self._balance = balance
    def get_display(self):
        return self._account_number, self._account_name, self._balance

    def set_withdraw(self, amount):
        if 0 < amount < self._balance: 
            self._balance -= amount
            print (f"withdraw {amount} $ from balance")
        else: 
            print ('Invalid Withdraw Amount')
    def set_deposit(self, amount):
        if amount > 0: 
            self._balance += amount
            print (f"Deposit {amount} $ to balance")
        else:
            print ('Invalid Deposit Amount')
    def get_account_number(self):
        return self._account_number
    def get_account_name(self):
        return self._account_name
    def get_balance(self):
        return self._balance
    def set_balance(self, amount):
        if amount - self._balance >= 0 :
            self._balance = amount - self._balance
        else:
            print("Invalid number")

My_tech_acc = BankAccount("190320xxxx", 'Sao Mai',20)
My_tech_acc.get_display()
My_tech_acc.set_withdraw(50)
My_tech_acc.set_deposit(20)