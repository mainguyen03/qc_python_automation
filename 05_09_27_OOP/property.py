class BankAccount():
    def __init__(self, account_number, account_name, balance = 1_000_000_000):
        self._account_number = account_number
        self._account_name = account_name
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount - self.balance >= 0 :
            new_balance = amount - self.balance
            self.balance = new_balance
        else:
            print("Invalid number")

    def get_display(self):
        return self.account_number, self.account_name, self.balance

    def set_withdraw(self, amount):
        if 0 < amount < self.balance: 
            new_amount = self.balance - amount
            self.balance = new_amount
            print (f"withdraw {amount} $ from balance")
        else: 
            print ('Invalid Withdraw Amount')

    def set_deposit(self, amount):
        if amount > 0: 
            new_amount = self.balance + amount
            self.balance = new_amount
            print (f"Deposit {amount} $ to balance")
        else:
            print ('Invalid Deposit Amount')
    

My_tech_acc = BankAccount("190320xxxx", 'Sao Mai',20)
My_tech_acc.get_display()
My_tech_acc.set_withdraw(50)
My_tech_acc.set_deposit(20)