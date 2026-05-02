class Bank:
    def __init__(self,balance,accountnumber):
        self.balance = balance
        self.accountnumber = accountnumber

    def debit(self, amount):
         self.balance -= amount
         print("Rs.",amount,"was debited")
         print("Total = Rs. ",self.balance)



    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"is credit")
        print("Total = Rs.",self.balance)



    
   


user1 = Bank(10000, 45678)
user1.debit(2000)
user1.credit(10000)
user1.credit(49000)
        