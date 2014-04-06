def laceStringsRecur(s1, s2):

	def helpLaceStrings(s1, s2, out):

		if s1 == "":
			return out + s2

		if s2 == "":
			return out + s1

		else:
			return s1[0] + s2[0] + laceStringsRecur (s1[1:],s2[1:])

	return helpLaceStrings(s1,s2,"")

s1 = "abcdefghijklam"
s2 = "123456"

print laceStringsRecur(s1,s2)