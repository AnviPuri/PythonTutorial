class Bank():

    def __init__(self,owner,balance):

        self.owner = owner
        self.balance = balance

    def deposit(self,amount):

        self.balance = self.balance + amount
        return f"Amount added with new balance as {self.balance}"

    def withdraw(self,amount):

        if amount > self.balance:
            return "Cannot withdraw as amount exceeds balance."

        self.balance = self.balance - amount
        return f"Amount deducted with new balance as {self.balance}"

bank = Bank("Mandy",10000)
print(bank.deposit(2000))
print(bank.withdraw(3000))

bank_two = Bank("Sandy",2000)
print(bank_two.withdraw(3000))