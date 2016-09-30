__author__='minal'
def fact_for_loop():
	n=input('enter the number')
	fact=1
	for i in range(n):
		i+=1
		fact=fact*i
	print 'factorial',fact

if __name__=='__main__':
	fact_for_loop()
