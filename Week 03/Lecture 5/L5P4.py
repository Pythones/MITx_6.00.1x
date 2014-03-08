def cgdIter (a, b):
	#Caso mas simple
	if a % a == 0:
		return a == 1
	if a % a - 1 == 0:
		return cgdIter (a-1)

print cgdIter (12)