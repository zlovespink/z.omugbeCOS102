# Calculation of annuity plan

#enter payment per time
PMT = float(input("How much did you pay per period? :"))

#enter Rate
R = float(input("What is you annaul interest rate? :"))

#enter number of times interest was compounded annualy
N= int(input("How many times was the interest compounded annualy? :"))

# enter the amount of years for annual compound interest
T= float(input("What number of years? :"))

Numerator = ((1 + (R/N)) ** (N * T)) - 1
Denominator = (R/N)
AnnuityPlan = PMT * (Numerator/Denominator)

print("Your Annuity plan is : N",AnnuityPlan )