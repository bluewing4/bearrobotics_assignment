import datetime as dt

a = dt.datetime.now() # 현재 일시
dateTime = a.strftime('%Y-%m-%d %H:%M:%S')

class ATM():
    def __init__(self, card_num, card_pin, account_num, balance):
        self.card_num = card_num
        self.card_pin = card_pin
        self.account_num = account_num
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print('==============================')
        print(dateTime)
        print(f"{amount} $ deposit successful!")
        print('==============================')
        print(f"Card No.{self.card_num}")
        print(f"No.{self.account_num} Account balance : {self.balance} $")
        print('==============================')

    def withdraw(self, amount):
        self.amount = amount
        if self.amount > self.balance:
            print('====================================')
            print(dateTime)
            print("Insufficient balance!")
            print(f"Card No.{self.card_num}")
            print(f"No.{self.account_num} Account balance : {self.balance} $")
            print("Try with lesser amount than balance.")
            print('====================================')
        else:
            self.balance -= amount
            print('=================================')
            print(dateTime)
            print(f"{amount} $ withdrawal successful!")
            print('=================================')
            print(f"Card No.{self.card_num}")
            print(f"No.{self.account_num} Account balance : {self.balance} $")
            print('=================================')

    def check_balance(self):
        print('==============================')
        print(dateTime)
        print(f"Card No.{self.card_num}")
        print(f"No.{self.account_num} Account balance : {self.balance} $")
        print('==============================')

        
    def menu(self):
        if login == True:
            print("""
            ====Bank Menu====
            1 = Check Balance
            2 = Deposit
            3 = Withdraw
            4 = Quit
            =================
            """)
            choice = int(input(' please Enter 1, 2, 3, 4 : '))
            if choice == 1:
                atm.check_balance()
                atm.menu()
            elif choice == 2:
                print('*********Deposit Menu*********')
                amount = int(input('Enter the cash to deposit: '))
                atm.deposit(amount)
                atm.menu()
            elif choice == 3:
                print('**********Withdraw Menu**********')
                amount = int(input('Enter the amount want to take: '))
                atm.withdraw(amount)
                atm.menu()
            elif choice == 4:
                print('Thanks for using ATM service ')
                #break
            else:
                print('=======================')
                print('    Invalid input')
                print('=======================')
                atm.menu()
     
               
login = False
login_num = 0  
pinok = False
tests = [
    {'card' : 12341234, 'pin' : 1234, 'account' : {1:100, 2:1200, 3:13000, 4:3000}},
]


while login == False:
    for test in tests:
        card = int(input('Please insert your card : '))
        while pinok == False:
            pin = int(input('Enter the pin number : '))
            # if card != test['card']:
            #     print('2')
            #     print('Card is not exist.')
            #     continue
            
            # else:
            #     print('3')
            #     pin = int(input('Enter the pin number : '))

            if pin != test['pin']:
                login_num += 1
                print(' Wrong Pin Number! how many %s' % (3 - login_num))
                pinok = False
                if login_num == 3:
                    print(' Sorry, Please come again tomorrow ')
                    exit()

            elif card == test['card'] and pin == test['pin']:
                print(' log in successfully!')
                pinok = True
                login = True
                print("ACCOUNT LIST:", list(test['account']))
                account_num = int(input("PLEASE SELECT AN ACCOUNT: "))
                balance = test['account'][account_num]
                card_num = card
                card_pin = pin
                atm = ATM(card_num, card_pin, account_num, balance)
                atm.menu()
                break

