__author__='minal'
def main():
    n=input('enter the number of the dictionary elements')
    dictionary=dict()
    for key in xrange(1,n):
        dictionary.update({key:key**2})

    print dictionary

if __name__=='__main__':
    main()

