balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04


#Monthly interest rate= (Annual interest rate) / 12.0
Mir = annualInterestRate/12
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Mmp = 0
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Mub = 0
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
Ubm = 0

#Setting Total Paid before de loop
TMmp = 0


for i in range (1,13):
       
    #Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
    Mmp = monthlyPaymentRate * balance
    
    #Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Mub = balance - Mmp
    
    #Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    Ubm = Mub + Mub*Mir
    
    balance = Ubm
    
    print "Month: " + str(i)
    print "Minimum monthly payment: " + str(round(Mmp,2))
    print "Remaining balance: " + str(round(Ubm,2))
    
    TMmp = TMmp + Mmp
    
 
print "Total paid: " + str(round(TMmp,2))
print "Remaining balance: " + str(round(Ubm,2))