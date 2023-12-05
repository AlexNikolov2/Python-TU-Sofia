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



def main():
    account_number = input("Account Number:")
    balance = int(input("Balance:"))
    pin = int(input("PIN code:"))
    
    bank = Account(account_number, balance, pin)
     
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
            print(bank.deposit(amount))
        elif(number == 2):
            pin = int(input('Set pin'))
            if(bank.pin == pin):
                print('Correct pin')
                amount = int(input('set amount '))
            else:
                print('Invalid pin')
            print(bank.draw(pin, amount))
        elif(number == 3):
            print(bank.account_info())
            break
main()  
        
        