__author__='minal'
def divide(x,y):
    try:
        result=x/y
    except Exception, e:
        print 'Exception is',e
    else:
        print 'result is',result
    finally:
        print 'executing finally block'

if __name__=='__main__':
    n=input('enter 1st number')
    m=input('enter 2nd number')
    divide(n,m)