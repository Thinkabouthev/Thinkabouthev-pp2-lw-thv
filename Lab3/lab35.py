class bank_account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
        print(f'name: {self.owner} \nbalance: {self.balance}')
        pass
    
    def deposit(self, money):
        self.balance += money
        print(f"deposit: {self.balance}")
    
    def withdraw(self, money):
        if self.balance - money >= 0:
            self.balance -= money
            print(f"Your balance: {self.balance}")
            return
        else:
            print(f'doesn\'t enough, you have only - {self.balance}tg')
            return


client = bank_account(input(), int(input()))
client.__init__

client.deposit(int(input()))
client.deposit

client.withdraw(int(input()))
client.withdraw

client.withdraw(int(input()))
client.withdraw