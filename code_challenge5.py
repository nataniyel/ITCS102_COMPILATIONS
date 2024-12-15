#inputs of grades

prelim = eval(input("Please enter your Prelim grade : "))
midterm = eval(input("Please enter your Midterm grade : "))
semi_final = eval(input("Please enter your Semi Final grade : "))
final = eval(input("Please enter your Final grade : "))
quiz = eval(input("Please enter your Quiz grade : "))
project = eval(input("Please enter your Project grade : "))

#computation of final grade

fg = (prelim*0.15) + (semi_final*.15) + (midterm*0.15) + (final*0.15) + (quiz*0.25) + (project*0.15)

#decision making

if fg >= 75 :
    print()
    print("Congratulations on passing!")
    print(f"Your total grade of {fg} has exceeded the passing grade of 75 making you eligible to pass this school year.")
else:
    print()
    print("Sorry, you have failed this school year.")
    print(f"Your final grade was {fg}%.")