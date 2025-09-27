from random import randint

class Bank:
    def __init__(self):
        self.account = randint(100,999) #generating rnadom number btw them.
        self.full_name = input("Enter name = ")
        self.phone_number = int(input("Enter phone number = "))
        self.balance = 0

    def show_info(self):
        print(f"Account number = {self.account}") 
        print(f"Full name = {self.full_name}")
        print(f"Phone number = {self.phone_number}")  
        print(f"Balance = {self.balance}\n") 

    def show_balance(self):
        print(f"Current balance = {self.balance}")

    def withdraw(self):
        amount = int(input("enter amount to withdraw = "))
        if amount > self.balance:
            print("Insucfficient balance")
        else:
            self.balance -= amount
    
    def deposit(self):
        amount = int(input("Enter amount to deposit = "))
        self.balance = self.balance + amount
'''
b1 = Bank()
b1.show_balance()
b1.deposit()
b1.show_balance()
b1.withdraw()
b1.show_balance()
'''

'''
banks = []
x = Bank()
banks.append(x)
print(banks) 
x = Bank()
banks.append(x)
print(banks)

banks[0].show_balance()
banks[1].deposit()
banks[1].show_balance()
'''


banks = []

def check_account_esixts(acc_no:int):
    global banks
    for obj in banks:
        if obj.account == acc_no:
            return obj
    return None


while True:
    print("\n1. Create Account")
    print("2.Show all bank details")
    print("3.Deposit")
    print("4.Withdrawal")
    print("5.Transfer")
    print("6.Exit\n")

    Choice = int(input("Enter choice  = "))
    if Choice == 1:
        obj = Bank()
        banks.append(obj)
    
    elif Choice == 2:
        if len(banks) == 0:
            print("\nNo accounts have been created yet :\n")
        else:
            for account in banks:
                account.show_info()
        
    elif Choice == 3:
        if len(banks) == 0:
            print("\nNo accounts have been created yet :\n")
        else:
            acc_no = int(input("Enter account number to deposit = "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.deposit()
                    break
  
    elif Choice == 4:
        if len(banks) == 0:
            print("\nNo accounts have been created yet :\n")
        else:
            acc_no = int(input("Enter account number to Withdrawal = "))
            for obj in banks:
                if obj.account == acc_no:
                    obj.withdraw()

    elif Choice == 5:
        form_acc_no = int(input("Enter account from which you want to transfer =  "))
        to_acc_no = int(input("Enter account to which you want to transfer =  "))

        from_acc_obj = check_account_esixts(form_acc_no)
        to_acc_obj = check_account_esixts(to_acc_no)

        if from_acc_obj != None and to_acc_obj != None:
            transfer_amount = int(input("Enter transfer amount = "))
            if from_acc_obj.balance < transfer_amount:
                print("\nInsufficient balance")
            else:
                from_acc_obj.balance -= transfer_amount
                to_acc_obj.balance += transfer_amount
            
        else:
            print("\nAccount number does not exists ")

    elif Choice == 6:
        break

    else:
        print("\nInvalid Choice")

 