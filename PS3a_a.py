def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

##################################
#Code to paste
##################################

def radiationExposure(start, stop, step):

	intNumSteps =  int((stop-start)/step)
	dblresult = 0

	for i in range(intNumSteps):
		
		x = start+(i*step)
		dblresult += f(x)*step
		#print dblresult

	return dblresult

##################################

print radiationExposure(0, 4, 0.25)
#print f(1)