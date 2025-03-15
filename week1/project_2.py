#calculating compound interest

#enter principal
P= int(input("What is your principal? : "))

#enter rate
R = float(input("What is your rate? :"))

#enter number of times interest is compounded each year
N= int(input("How many times ? :"))

#enter Time
T = float(input("How long? : "))

Amount = P * (( 1+ (R/N))** (N*T))

CompoundInterest = Amount - P

print("Your compound interest is : N", CompoundInterest)