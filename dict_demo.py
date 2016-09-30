__author__='minal'
def average_stud():
	students=[{'name':'xyz','marks':12},{'name':'pqr','marks':56}]
	a=0
	for stud in students:
		a=a+stud['marks']
	print 'average',a/len(students)
if __name__=='__main__':
	average_stud()
