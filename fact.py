__author__='minal'
def factorial():
    a=input('Enter Number')
    fact=1
    while a>0:
        fact=fact*a
        a=a-1
    print('factorial ',fact)
if __name__ == "__main__":
    factorial()
