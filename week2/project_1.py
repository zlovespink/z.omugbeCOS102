for var1 in range(3):
    print("Iteration " + str(var1 + 1) + " of outer loop")
    for var2 in range(2): #nested loop
        print(var2 +1)
    print("out of inner loop")
print("out of inner loop")
