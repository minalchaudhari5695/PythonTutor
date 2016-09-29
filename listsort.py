__author__='minal'
def list_sort():
	sample=[['abc',26.66],['qwe',45.67],['hgj',34.12],['ABD',98.8]]
	print sample
	sample.sort()
	for i in sample:
		a=i[0]
		b=i[1]
		print a, b,'%'
if __name__=='__main__':
	list_sort()
