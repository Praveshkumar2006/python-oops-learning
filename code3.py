class PNB: 
    #defing the self
    def __init__(self, account, balance): #object attribute

        self.account = account
        self.balance = balance
    def debit(self, amount):
        self.balance -= amount
        print("Rs.", amount, "was debited")
        print("Total balance =", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("Total balance =", self.get_balance())
    def get_balance(self):
        return self.get_balance


payment1 = PNB("JPR", 1000000)
payment1.debit(500)
payment1.credit(50000)
print(payment1.account, payment1.balance)

print("GOOD JOB")