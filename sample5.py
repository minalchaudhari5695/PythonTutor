__author__='minal'

def expr_check():
    a=input('enter a')
    b=input('enter b')
    c=input('enter c')
    n=input('enter n')
    if a**n+b**n == c**n:
        print 'equal'
    else:
        print'not equal'

if __name__== "__main__":
    expr_check()

