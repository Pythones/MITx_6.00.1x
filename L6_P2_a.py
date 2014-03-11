tplTest = (1,2,3,4,5,6)

def oddTuples(aTup):

	counter = 1
	tplOdss = ()


	for a in aTup:

		if counter%2 != 0:
			tplOdss += (a,)

		counter += 1

	return tplOdss

print oddTuples(tplTest)

