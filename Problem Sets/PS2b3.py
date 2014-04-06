balance = 3457
annualInterestRate = 0.15


#Monthly interest rate= (Annual interest rate) / 12.0
Mir = annualInterestRate/12
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Mmp = 0
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Mub = 0
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
Ubm = 0


#Setting Variables before de loop
oldbalance = balance


while balance > 0:

    Mmp += 10
    balance = oldbalance
    Count = 0
    

    #going trough months
    while Count < 12:
           
        Count += 1
        balance -= Mmp
        balance += Mir * balance


print "Lowest Payment: " + str(Mmp)