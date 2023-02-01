def factorial(n):
	"A recursive implementation of the factorial function"
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)