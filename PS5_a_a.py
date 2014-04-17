def recur(n):
    a = 0

    if n<=1:
        return 1

    else:
        a += 1
        b = n*recur(n-1)

    return a


for i in range(10):

    print recur(i)

