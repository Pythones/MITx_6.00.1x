#PS2_P2

balance = 4773
annualInterestRate = 0.2


dblmonthlyRate = annualInterestRate/12
mmp = 0
dblBalanceBackup = balance

while balance >0:

	mmp += 10
	balance = dblBalanceBackup
	counter = 0

	while counter<12 and balance >0:

		counter += 1
		balance -= mmp
		balance += dblmonthlyRate*balance

	#print balance
print 'Lowest Payment: ' + str(mmp)