class Account:
    def __init__(self, account_number, balance, pin):
        self.account_number = account_number
        self.balance = balance
        self.pin = pin
        
    def print_info(self):
        print("Account number: ", self.account_number)
        print("Balance: ", self.balance)
        print("PIN: ", self.pin)
    def deposit(self, amount):
        if(amount <= 0):
            print('Invalid amount')
        self.balance += amount
        print(f"Deposit {amount} into the bank account.")
        print(f"Balance now: {self.balance}")
    def draw(self, pin, amount):
            if(self.pin == pin):
                print('correct pin')
            if(amount > self.balance):
                print('invalid amount!')
            else:
                self.balance -= amount
                print(f"Withdrew {amount} from bank account.")
                print(f"Balance: {self.balance}")
    def account_info(self):
        print('account number:', self.account_number)
        print('balance:', self.balance)

class SavingsAccount(Account):
    def __init__(self, account_number, balance, pin, interest_rate):
        self.interest_rate = interest_rate
        super().__init__(account_number, balance, pin)
    def calculate_interest(self):
        interest = self.interest_rate * self.balance
        print('interest:', interest)
        return interest
    def calculate_balance_with_interest(self):
        print('balance:', self.balance)
        print('interest:', self.interest)
    def account_info(self):
        print('account number:', self.account_number)
        print('balance:', self.balance + self.calculate_interest())

def main():
    account_number = input("Account Number:")
    balance = int(input("Balance:"))
    pin = int(input("PIN code:"))
    
    #bank = Account(account_number, balance, pin)
    
    bank_type = input("Bank Type:")
    if(bank_type == 'savings'):
        interest_rate = float(input("Interest Rate"))
        account = SavingsAccount(account_number, balance, pin, interest_rate)
    else:
        account = Account(account_number, balance, pin)
    while(True):
        print('==================')
        print('MENU')
        print('==================')
        print('1. Deposit')
        print('2. Draw')
        print('3. Account Info')
        number = int(input('Set number'))
        if(number == 1):
            amount = int(input('Set amount'))
            print(account.deposit(amount))
        elif(number == 2):
            pin = int(input('Set pin'))
            if(account.pin == pin):
                print('Correct pin')
                amount = int(input('set amount '))
            else:
                print('Invalid pin')
            print(account.draw(pin, amount))
        elif(number == 3):
            if(bank_type == 'savings'):
                print(account.account_info())
            else:
                print(account.account_info())
            break
main()