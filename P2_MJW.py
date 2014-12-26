# Sum even terms of Fibonacci sequence to n

phi = ((1+5**0.5)/2.0)**3
lim = input('Enter the upper limit: ')
k = 2
sum = k

while k < lim:
	k = round(k*phi,0)
	if k > lim:
		break
	sum = sum+k
	
print sum