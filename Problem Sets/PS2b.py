# -*- coding: utf-8 -*-
balance = 3892
annualInterestRate = 0.04


#Monthly interest rate= (Annual interest rate) / 12.0
Mir = annualInterestRate/12
#Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
Mmp = 0
#Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
Mub = 0
#Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
Ubm = 0


#Setting Total Paid before de loop
oldbalance = balance
Count = 0
n = 1

while True:
    
    #Minimum monthly payment = guess it!
    Mmp = n * 10
    #print Mmp
    
    #Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
    Mub = oldbalance - Mmp
    
    #Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)
    Ubm = Mub + (Mub*Mir)
    
    #si Ubm después de 12 meses no es cero o menor que cero, incrementamos 10 y pasamos 12 veces más
    
    Count = Count + 1
    oldbalance = Mub
    
    if Count == 11:
        if Ubm <= 0:
            print "Lowest Payment: " + str(Mmp)
            break
        else:
            Count = 0
            n = n + 1
            oldbalance = balance
            #print balance