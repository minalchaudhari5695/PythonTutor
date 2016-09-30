__author__='minal'
def list_fuction():
	l=list()
	l.insert(0,1)
	l.insert(1,2)
	print l
	l.remove(2)
	print l
	l.append(5)
	print l
	l.sort()
	print l
	l.reverse()
	print l

if __name__== "__main__":
	list_fuction()
