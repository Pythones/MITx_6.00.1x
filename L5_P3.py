#Second recursive exponential

def recurPowerNew(base, exp):

    if exp <= 0:

        return 1

    elif exp%2 != 0:

        return base*(recurPowerNew(base,exp-1))

    else: return recurPowerNew(base*base,exp/2)

print recurPowerNew(2,4)