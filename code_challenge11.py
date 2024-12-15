#Diamond shape for loop

# first top part
#range value 1 is the starting point, while 'yung 12 + 1 is gaano kalaki 'yung shape ng diamond

for i in range(1, 3 + 1):
    print("  " * (3 - i), end=" ")
    print("* " * (i * 2 - 1))
for i in range(3 - 1, 0, -1):
    print("  " * (3 - i), end=" ")
    print("* " * (i * 2 - 1))

    
    