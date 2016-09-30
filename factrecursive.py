__author__='minal'
def fact_rec():
	n=input('enter the number')
	f=fact(n)
	print 'factorial',f
def fact(n):
	if n==0:
		return 1
	else:
		return n*fact(n-1)

if __name__=='__main__':
	fact_rec()
