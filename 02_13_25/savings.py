class SavingsAccount:
    RATE = 0.02
    def __init__(self, name, pin, balance=0.0):
        self.name = name
        self.pin = pin
        self.balance = balance
    
    def __str__(self):
        name_lbl = 'Name:'
        pin_lbl = 'PIN:'
        bal_lbl = 'Balance:'
        result = f"{name_lbl:10}{self.name}\n{pin_lbl:10}{self.pin}\n{bal_lbl:10}{self.balance}"
        #result += 'PIN:     ' + self.pin + '\n'        
        #result += 'Balance:     ' + str(self.balance)
        return result
    def get_balance(self):
        return self.balance
    def get_name(self):
        return self.name
    def deposit(self, amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount < 0:
            return "Amount must be >= 0"
        elif self.balance < amount:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return None
    def compute_interest(self):
        interest = self.balance * SavingsAccount.RATE
        self.deposit(interest)
        return interest
    
    
account = SavingsAccount("Harry Potter", "934", "2000")
print(account)
