def laceStringRecur(s1,s2):

    def helpLaceStrings(s1,s2,out):

        if s1 == '':
            return out + s2

        if s2 == '':
            return out + s1

        else:
            return s1[0] + s2[0] + laceStringRecur(s1[1:],s2[1:])

    return helpLaceStrings(s1,s2,'')

s1 = 'abcd'
s2 = '123456'

print laceStringRecur(s1,s2)


