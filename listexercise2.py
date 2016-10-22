__author__='minal'

def string_get():
    
    list2=['abc','mam','aa','asda','a','121']
    abc=[x for (i,x) in enumerate(list2) if i not in (0,2,4)]
    print abc

if __name__=='__main__':
    string_get()