balance = 999999
annualInterestRate = 0.18
	      

#Setting Variables before de loop
oldbalance = balance #Avoid loosing original balance during de loop
Mir = annualInterestRate/12 #Monthly interest rate= (Annual interest rate) / 12.0
Mmp = 0 #Minimum monthly payment, we are trying to guess these value

#min and max Mmp value
MmpMin = balance/12
MmpMax = (balance * (1+ annualInterestRate))/12


while True:
    
    Count = 0
    balance = oldbalance
    Mmp = (MmpMax+MmpMin)/2
    #print Mmp

    #going trough every month from one year
    while Count < 12:
            
        Count = Count + 1
        balance = balance - Mmp
        balance = balance + (Mir * balance)
        #print Count
        #print balance
    
    if MmpMax - MmpMin <= 0.01:
        print "Lowest Payment: " + str(round(Mmp,2))
        break  
        
    elif balance < 0:
        MmpMax = Mmp
        #print "balance mayor que cero " + str(Mmp)
            
    elif balance > 0:
        MmpMin = Mmp
        #print "balance menor que cero " + str(Mmp)
        #print MmpMin