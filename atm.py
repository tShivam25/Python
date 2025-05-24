#This is a code for creating simple ATM system. I have made this using basic OOP concept while practicing my python skills.
#To run this code-> Account Number=1234567890
#                   Pin=1234

import time 
import sys

class Atm:
    def __init__(self):
        self.account_number=1234567890
        self.pin=1234
        self.balance=25000
        self.landing()

    def landing(self):
            print("|||        Circle Card Welcomes You!        |||")
            check_acc=int(input("Enter your account number: "))
            check_pin=int(input("Enter your pin: "))
            if check_pin==self.pin and check_acc==self.account_number:
                self.load()
            else:
                print("Incorrect pin or account number entered ! (^_^)")

    def load(self):
        print("Fetching your details" , end="")
        for i in range(6):
            print(".",end="")
            time.sleep(1)
        print(end="\n")
        self.details()

    def details(self):
        print("Hello, Mr. XYZ! \n Welcome to Circle Card ATM services!")
        print("Account number: ", self.account_number)
        print("Available Balance: ", self.balance)
        self.menu()
        
    def menu(self):
        user_input=int(input("""
        How can I help you?
        Press 1 to Withdraw.
        Press 2 to Desposit.
        Press 3 to Change Pin.
        Press 4 to Exit.
        """))
        
        if user_input==1:
            self.Withdraw()
        elif user_input==2:
            self.Deposit()
        elif user_input==3:
            self.ChangePin()
        elif user_input==4:
            self.Exit()
        else:
            print("Invalid Input!!")
    
    def ChangePin(self):
        print("Let's change pin of your Bank Account.")
        current_pin=int(input("Enter your old pin:"))
        if(current_pin==self.pin):
            new_pin=int(input("Enter new pin:"))
            self.pin=new_pin
        else:
            print("The pin you entered is incorrect.")   
        self.menu()
    
    def Withdraw(self):
        amt=int(input("Enter the amount you want to withdraw:"))
        if(amt<=self.balance):
            self.balance-=amt
            print("Withdrawal Amount: ", amt, "\n", "Amount left in Bank Account: ", self.balance)
        else:
            print("You can't withdraw the entered amount: ")
        self.menu()
    
    def Deposit(self):
        deposit_amt=int(input("Enter the amount to be deposited: "))
        self.balance+=deposit_amt
        print("Amount deposited: ", deposit_amt)
        print("Account Balance: ", self.balance)
        self.menu()
    
    def Exit(self):
        print("Thank you for visiting us", end="")
        for i in range(5):
            print("!", end="")
            time.sleep(1)
        
user=Atm()

