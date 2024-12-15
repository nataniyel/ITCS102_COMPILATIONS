#inputs

name = input("What is your name? : ")
age = int(input("Please enter your age : "))

#printing age chart

print("""
        0 Ano ka?
        1 - 8 Toddler
        9 - 18 Preteen
        15 - 18 Teenager
        19 - 27 Early Adulthood
        28 - 44 Middle Age
        45 - 59 Post Adulthood
        60 - 99 Senior
        100 - 150 Lakas mo po
        151+ Grabeng henerasyon naabutan mo
""")

#conditions
if age == 0:
    print(f"Hi {name}, HOOWWWWW?!.")
elif age >= 1 and age <= 8:
    print(f"Hi {name}, your are a Toddler.")
elif age >= 9 and age <= 18:
    print(f"Hi {name}, your are a Preteen.")
elif age >= 15 and age <= 18:
    print(f"Hi {name}, your are a Teenager.")
elif age >= 19 and age <= 27:
    print(f"Hi {name}, your are in your Early Adulthood.")
elif age >= 28 and age <= 44:
    print(f"Hi {name}, your are in your Middle Age.")
elif age >= 45 and age <= 59:
    print(f"Hi {name}, your are in your Post Adulthood.")
elif age >= 60 and age <= 99:
    print(f"Hi {name}, your are a senior.")
elif age >= 100 and age <= 150:
    print(f"Hi {name}, Lakas mo po.")
else :
    print("Kumusta panahon ng mga espanyol?")