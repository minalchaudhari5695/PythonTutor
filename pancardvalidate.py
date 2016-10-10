__author__='minal'
def check_no():
	a=raw_input('Enter the PAN card number\n')
	a=a.upper()
	print a
	if len(a)!=10:
		print 'Invalid Input'
	if a[0:4].isalpha() and a[5:8].isdigit() and a[9].isalpha():
		if a[4]=='P' or a[4]=='F' or a[4]=='C':
			print 'Valid pan card number'					
		else:
			print 'Invalid pan card number'
		
if __name__=='__main__':
	check_no()