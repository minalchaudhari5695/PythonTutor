__author__='minal'
class Dog:
    kind ='sample string'
    def __init__(self,name):
        self.name=name
def main():
    d=Dog('abc')
    print d.kind

if __name__=='__main__':
    main()
