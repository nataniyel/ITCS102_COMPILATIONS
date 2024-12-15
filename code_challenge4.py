
#Kuha muna ng data na i cacalculate
name = input("Please enter your name : ")
deposit = eval(input("Enter the amount you want to deposit : "))

#calculation ng denominations
print("Hello,", name, ",here is the denomination breakdown on the amount you deposited : ")

one_thousand = deposit // 1000
print("P%i| -------->   %i" % (1000, one_thousand))
sukli = deposit % 1000

five_hundred = sukli // 500
print("P%i | -------->   %i" % (500, five_hundred))
sukli = sukli % 500

two_hundred = sukli // 200
print("P%i | -------->   %i" % (200, two_hundred))
sukli = sukli % 200

one_hundred = sukli // 100
print("P%i | -------->   %i" % (100, one_hundred))
sukli = sukli % 100

fifty = sukli // 50
print("P%i  | -------->   %i" % (50, fifty))
sukli = sukli % 50

twenty = sukli // 20
print("P%i  | -------->   %i" % (20, twenty))
sukli = sukli % 20

ten = sukli // 10
print("P%i  | -------->   %i" % (10, ten))
sukli = sukli % 10

five = sukli // 5
print("P%i   | -------->   %i" % (5, five))
sukli = sukli % 5

one = sukli // 1
print("P%i   | -------->   %i" % (1, one))
sukli = sukli % 1