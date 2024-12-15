#Nathaniel Allapitan Bank Simulation
import os
balance = 0
#Denom fucntion
def denom():
    print("-----------------------------------------------------------")
    print()
    print("Here is the Philippine Currency Denominations : ")
    print()
    print("1000  ------> 0")
    print("500   ----->  0")
    print("200   ----->  0")
    print("100   ----->  0")
    print("50    ---->   0")
    print("20    ---->   0")
    print("10    ---->   0")
    print("5     --->    0")
    print("1     --->    0")
    print()
    print("-----------------------------------------------------------")
#When depositing, we can breakdown also the denominations here using for loop
def deposit():
    global balance
    deno =  (1000, 500, 200, 100, 50, 20, 10, 5, 1)
    os.system('cls')
    denom()
    while True:
        print(f"This is your current balance : P{balance}.00")
        depo = input(f"Please enter the amount you want to deposit : P")
        if depo.isdigit():
            os.system('cls')
            depo = int(depo)
            balance += depo
            print(f"Congratulations on your deposit! Here is your new balance P{balance}.00")

            again = input("Do you want to deposit again? ( Y | N ) : ")
            if again.lower() == "y":
                continue
            elif again.lower() == "n":
                print("Thank you for trusting us!")
                print("-----------------------------------------------------")
                print()
                print("Here is the bill breakdown for your deposit amount : ")
                for d in deno:
                    count = depo // d
                    print("P%i ------>    %i" % (d, count))
                    depo -= count*d
                print()
                print("-----------------------------------------------------")
                print()
                break
            else:
                print("That's an invalid input, the process has been terminated please try again. ")
                break
        else:
            print("Please put a valid amount!!!")
    return depo
#Money withdrawal here sir
def withdraw():
    global balance
    os.system('cls')
    while True:
        print(f"This is your current balance P{balance}.00")
        withdraw = input(f"Please enter the amount you want to withdraw : P")
        if withdraw.isdigit():
            os.system('cls')
            withdraw = int(withdraw)
            if withdraw <= balance:
                balance -= withdraw
                print(f"Congratulations on your withdrawal! Here is your new balance P{balance}.00")
                
                again = input("Do you want to withdraw again? ( Y | N ) : ")
                if again.lower() == "y":
                    continue
                elif again.lower() == "n":
                    print("Thank you for trusting us!")
                    os.system('cls')
                    break
                else:
                    print("That's an invalid input, the process has been terminated please try again. ")
                    break
            else:
                print("You don't have enough balance to withdraw!")
        else:
            print("Please put a valid amount!!!")
    return withdraw
#the main function with all the contents

def get_started():
    global balance
    print(f"Good day! Welcome to our bank.")
    create = input("Do you want to make a bank account with us? ( Y | N ) : ")

    if create.lower() == "y":
        os.system('cls')
        name = input("Please enter your name : ")
        print(f"Hi {name}, your account has been succesfully created. ")
        os.system('cls')
        while True:
            print("How would you like to proceed?")
            print("------------------------------")
            print()
            print("1----- Deposit")
            print("2----- Withdraw")
            print("3----- Balance")
            print("4----- Exit")
            print()
            print("------------------------------")

            choice = input("Please select a procedure you want to do : ")

            if choice == "1":
                deposit()
            elif choice == "2":
                withdraw()
            elif choice == "3":
                os.system('cls')
                print(f"Your balance is P{balance}.00")
            elif choice == "4":
                print("Thank you for using our service! Come again")
                break
    else:
        print(f"Okay, thank you for coming!")


get_started()



