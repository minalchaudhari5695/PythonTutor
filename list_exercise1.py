""" list exercise"""
__author__='minal'
__version__=1.0
def main():
    count=0
    strlist=['abc','mam','aa','asda','a','121']
    print 'the number of strings having length greater than 1 and first and last letter must be same\n'
    print strlist
    for i in strlist:
        if len(i)>1 and i[0]==i[-1]:
                count=count+1

    print count

if __name__=='__main__':
    main()

