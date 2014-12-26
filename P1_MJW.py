# Finding sum of multiples of two numbers up to a limit

def highest_in_series(mul,maxi):
	n = maxi-1
	while n > maxi-(mul+1):
		if n%mul==0:
			return n
		else: n=n-1

def sum_terms(m1,l):
	mn = highest_in_series(m1,l)
	n = mn/m1
	return (n/2.0)*(m1+mn)
			
l = input('Enter an upper limit: ')
a1 = input('Enter the first multiple: ')
b1 = input('Enter the second multiple: ')
c1 = a1*b1

a = sum_terms(a1,l)
b = sum_terms(b1,l)
c = sum_terms(c1,l)

print a+b-c






