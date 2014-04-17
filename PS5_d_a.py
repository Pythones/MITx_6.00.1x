def program1(x):
	counter = 0
	total = 0
	counter += 1
	for i in range(1000):
		counter += 3
		total += i

	while x > 0:
		counter+=5
		x -= 1
		total += x

	return counter


print program1(3)