__author__='minal'
def sort_fun():
	a=[5,3,1,6,8]
	print a
	for i in range(len(a)-1):
		j=i
		for j in range (len(a)-i-1):
			if a[j]<a[j+1]:
				temp=a[j]
				a[j]=a[j+1]
				a[j+1]=temp
	print a
if __name__=='__main__':
	sort_fun()
