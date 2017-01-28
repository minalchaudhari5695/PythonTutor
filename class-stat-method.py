__author__='minal'
class Person:
    titles=('Dr','Mr','Mrs','Ms')
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname

    def fullname(self):#instance method
    #instance object accessible through self
        return "%s %s" % (self.name,self.surname)

    @classmethod
    def allowed_titles_starting_with(self, startswith):#class method
        #class or instance object accessible through self/cls
        return [t for t in self.titles if t.startswith(startswith)]

    @staticmethod
    def allowed_titles_ending_with(endswith):#static method
        #no parameters for instance or class object
        #we have to use Person directly
        return [t for t in Person.titles if t.endswith(endswith)]

def main():
    jane=Person("Jane","Smith")
    print(jane.fullname())
    print(jane.allowed_titles_starting_with("M"))
    print(Person.allowed_titles_starting_with("M"))
    print(jane.allowed_titles_ending_with("s"))
    print(Person.allowed_titles_ending_with("s"))

if __name__=='__main__':
    main()
