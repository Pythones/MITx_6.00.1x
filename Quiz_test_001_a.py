def laceString(s1,s2):

	intL1 = len(s1)
	intL2 = len(s2)
	s3 = ''

	for i in range(min(intL1,intL2)):

		ans = s1[i]+s2[i]
		s3 = s3 + ans

	if intL1 < intL2:
		s3 += s2[intL1-intL2:]
	elif intL1 == intL2:
		pass
	else:
		s3 += s1[intL2-intL1:]

	return s3

s1 = 'cj'
s2 = 'grxzdc'

print laceString(s1,s2)