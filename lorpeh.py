import random


def Account_generated(no_of_persons):
        Accounts = []
        for no in range(no_of_persons):
            accountnumber = random.randint(0000000000,9999999999)
            Accounts.append(accountnumber)
        return Accounts

class BankAccount:
    def __init__(self, accountnumber, name, balance):
        self.accountnumber = accountnumber
        self.name = name
        self.balance = balance

    def Deposit(self):
        amount = float(input("Enter amout to be deposited: "))
        self.balance+=amount
        return(f"Your deposit of {amount} has been processed, your balance is: {self.balance}")


    def Withdrawal(self):
        try:
            acct_gen = Account_generated(10)
            for acct in acct_gen:
                if acct == self.accountnumber:
                    print("continue transaction")
                    amount = float(input("Enter amout to withdraw: "))
                    if self.balance >=amount:
                        self.balance-=amount
                        return(f"Withrawal of {amount}is being processed, kindly take your cash")
                raise ValueError
        except Exception as e:
            print(f"sorry account number {self.accountnumber} does not exist", e)
    
Account = BankAccount('', 'Tolulope', 20000)
Account.Withdrawal()