__author__='minal'
def fibo_series():
    n=input('enter the range of the fibo series\n')
    ls1=[0]
    ls2=[0]
    a,b=0,1
    while n>1:
        a,b=b,a+b
        n-=1
        ls1.append(a)
        ls2.append(a**3)
    print ls1
    print ls2    
if __name__=='__main__':
    fibo_series()