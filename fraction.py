class Fraction:
    def __init__(self, x, y):
        if y == 0:
            print("Denominator cannot be zero")
        self.num = x
        self.den = y 

    def __str__(self):
        return "{}/{}".format(self.num, self.den)

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return "{}/{}".format(new_num, new_den)

    def __sub__(self, other):
        new_num = self.num * other.den - other.num * self.den
        new_den = self.den * other.den
        return "{}/{}".format(new_num, new_den)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return "{}/{}".format(new_num, new_den)

    def __truediv__(self, other):
        if other.num == 0:
            print("Cannot divide by zero")
        new_num = self.num * other.den
        new_den = self.den * other.num
        return "{}/{}".format(new_num, new_den)

n1 = int(input("Enter Numerator: "))
d1 = int(input("Enter Denominator: "))
fr1 = Fraction(n1, d1)
print("Your Fraction is:", fr1)
ch = input("Do you want to perform other operations on this fraction? (Y/N): ")
if ch.lower() == "y":
    n2 = int(input("Enter Numerator for another fraction: "))
    d2 = int(input("Enter Denominator for another fraction: "))
    fr2 = Fraction(n2, d2)
    opr = input("Enter the operation you want to perform (+, -, *, /): ")
    if opr == "+":
        print("Your Result is:", fr1 + fr2)
    elif opr == "-":
        print("Your Result is:", fr1 - fr2)
    elif opr == "*":
        print("Your Result is:", fr1 * fr2)
    elif opr == "/":
        print("Your Result is:", fr1 / fr2)
    else:
        print("Invalid input!!")

elif ch.lower() == "n":
        print("Okay!!!!")

else:
    print("Invalid Input!")

