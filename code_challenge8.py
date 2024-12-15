#odd and even

total = 0
odd = 0
even = 0

for k in range(1, 4):
    num = eval(input("Enter a number: "))
    total += num 
    if num % 2 == 0:
        even += num
    else:
        odd += num

print(f"The total is: {total}")
print(f"The even: {even}")
print(f"The odd: {odd}")