for a in range(1, 8):
    for b in range(a, 7 + 1):
        print(" ", end=" ")
    for c in range(1, a, +1):
        print("*", end=" ")
    for d in range(1, a, +1):
        print("^", end=" ")
    print()
for e in range(7, 0, -1):
    for f in range(e, 8):
        print(" ", end=" ")
    for g in range(1, e, +1):
        print("^", end=" ")
    for h in range(1, e, +1):
        print("*", end=" ")
    print()