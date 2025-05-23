import time 
import sys

class Atm:
    def __init__(self):
        self.pin=" "
        self.balance=0
        self.landing()

    def menu(self):
        user_input=input("""
        Hi how can I help you?
        Press 1 to create pin.
        Press 2 to change pin.
        Press 3 to check balance.
        Press 4 to Withdraw.
        Press 5 to EXIT.
        """)
        
        if user_input==1:
            self.CreatPin()
        elif user_input==2:
            self.ChangePin()
        elif user_input==3:
            self.CheckBalance()
        elif user_input==3:
            self.Withdraw()
        elif user_input==4:
            self.Exit()
        else:
            print("Invalid Input!!")
    
    def landing(self):
            print("Circle Card Welcomes You!")
            self.load()
        
    def load(self):
        load=['|', '/', '#']
        print("Fetching your details" , end="")
        for i in range(6):
            print(".",end="")
            time.sleep(1)
        self.details()

def details(self):
    user_pin="1234"
    user_balance=25000
    self.pin=user_pin
    self.balance=user_balance

    def CreatePin(self):
        print("Let's create pin for your Bank Account.")
        user_pin=int(input("Enter pin for your Bank Account:"))
        self.pin=user_pin
    
    def ChangePin(self):
        print("Let's change pin of your Bank Account.")
        current_pin=int(input("Enter your old pin:"))
        if(current_pin==self.pin):
            new_pin=int(input("Enter new pin:"))
            self.pin=new_pin
        else:
            print("The pin you entered is incorrect.")    
    
    def CheckBalance(self):
        print("Let's Check Balance of your account.")
        print("Your current balance is: ", self.balance)
    
    def Withdraw(self):
        amt=int(input("Enter the amount you want to withdraw:"))
        if(amt<=self.balance):
            self.balance-=amt
            print("Withdrawal Amount: ", amt, "\n", "Amount left in Bank Account: ", self.balance)
        else:
            print("You can't withdraw the entered amount: ")
    
    def Exit(self):
        print("Thank you for being with Circle Card!!")
            

user=Atm()
        