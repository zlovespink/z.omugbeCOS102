#calculation of simple interest

#enter principal
P= int(input("What is your principal? : "))

#enter Rate
R= float(input("what's your rate? : ")) / 100 # convert rate to rate/ 100 given as a float

#enter Time
T = float(input("How long? : "))

#simple interest formula given 
SimpleInterest = P * (1 + (R * T))

print ("Your simple interest is : N", SimpleInterest)
