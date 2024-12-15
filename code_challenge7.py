#Grocery
name = input("Please enter your name : ")
did_groceries = input("Did you buy grocery today? ( Yes | No ) : ")
#conditions
if did_groceries.lower() == "yes" :
    product = input("What product/s did you purchase today? : ")
    untaxed_price = eval(input("Total Price of purchased product : P"))
    vat = untaxed_price * 0.123
    taxed_price = untaxed_price + vat
    print(f"Your total price would be P{taxed_price} due to the VAT of 12.3%")
    payment = eval(input("How much would you be paying? : P"))
    change = payment - taxed_price 
    age = int(input("How old are you? : "))
    print()
    #Check price if more than 4000  
    if untaxed_price >= 4000:
        print("You have purchased more than P4000.00 and is eligible for a discount of 3.8%")
        discount = untaxed_price * 0.038
        disc_price = taxed_price - discount
        print(f"Your discounted total would be P{disc_price} due to the discount of 3.8%")
        print()
        disc_change = payment - disc_price
        if age >= 60 and age <= 150:
            senior_disc = taxed_price * 0.123
            senior_total = taxed_price - senior_disc
            print(f"Your total price with senior discount is P{senior_total}")
            change = payment - senior_total
            print(f"Your change would be P{round(change , 2)}")
        else:
            print("You are not qualified for a senior discount")
            print(f"Your change would be P{round(disc_change , 2)}")
            print("Thank you for shopping!") 
    else:
        print(f"Your change would be P{round(change , 2)}")
        print("Thank you for shopping!")
else:
    print("Thank you, come again!")