__author__='minal'
class Contact:
    all_contacts=[]
    def __init__(self, name):
        self.name=name
        self.all_contacts.append(name)

    def print_data(self,*args):
        print Contact.all_contacts

class Friend(Contact):
    def __init__(self,name,phone):
        Contact.__init__(self, name)
        self.phone=phone

def main():
    c=Contact('minal')
    print c.all_contacts
    f=Friend('Abc',123456)
    print f.name
    print f.phone
    c.print_data()

if __name__=='__main__':
    main()
        
        