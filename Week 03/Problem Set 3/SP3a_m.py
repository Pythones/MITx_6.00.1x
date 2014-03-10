def f(x):
    import math
    return 10*math.e**(math.log(0.5)/5.27 * x)

def radiationExposure(start, stop, step):

    intCount = int((stop-start)/step)
    ans = 0
    dist = stop

    #while stop - step >= start:
    for i in range (intCount):
        
        dist += - step
        #print dist
        ans += step * f(dist)
        #print ans

    return ans

print radiationExposure (40, 100, 1.5)