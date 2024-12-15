sum = 0
isRepeat = True

while isRepeat == True:
    num = eval(input("Please put a number : "))
    sum += num
    if num == 0:
        print(f"The sum of all the given numbers is : {sum}")
        break
    else:
        print('Add more number, you will get the sum when you put "0"')