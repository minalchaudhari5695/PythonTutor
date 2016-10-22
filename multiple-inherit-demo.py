__author__='minal'
class Contact:
    all_contacts=[]
    def __init__(self,name):
        self.name=name
        self.all_contacts.append(name)
class Marks:
    @classmethod
    def print_marks():
        print 'second subclass'
class Friend(Contact,Marks):
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
        self.all_contacts.append(name)
    @classmethod
    def print_method(self, *args):
        print Contact.all_contacts

def main():
    c=Contact('minal')
    print c.all_contacts
    f=Friend('Abc',123456)
    print f.name
    print f.phone
    f.print_method()
    f.print_marks()
    print issubclass(Friend,Contact)
    print isinstance(f,Friend)
if __name__=='__main__':
    main()
