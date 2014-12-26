# Find the highest prime factor of a number

def find_next_prime(list):
	new = list[-1]+1
	# check to see if it's divisible by anything in the list
	divisible=False
	while divisible==False:
		for x in list:
			if new%x==0:
				divisible=True
		# If it is, increment and reset 'divisible' variable
		if divisible==True:
			new=new+1
			divisible=False
		# If it isn't, add it to primes list
		else:
			list.append(new)
			return

def factored(num,primes):
	n=primes[-1]
	if num==n:
		return
	while num%n==0:	
		num=num/n
	find_next_prime(primes)
	factored(num,primes)
		
primes = [2]
num = input('Enter number: ');
factored(num,primes)
print primes[-1]


		

