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


class RestrictedSavingsAccount(SavingsAccount):
    TOTAL_WITHDRAWS = 3
    def __init__(self, name, pin, balance=0.0):
        super().__init__(name, pin, balance)
        self.withdraws = 0

    def withdraw(self, amount):
        if self.withdraws >= RestrictedSavingsAccount.TOTAL_WITHDRAWS:
            return "No more withdraws this month"
        else:
            self.withdraws += 1
        return super().withdraw(amount)
    
    def resetCounter(self):
        self.withdraws = 0
    
    
account = SavingsAccount("Harry Potter", "934", "2000")
print(account)
