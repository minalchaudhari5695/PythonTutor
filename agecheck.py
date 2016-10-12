__author__='minal'
import datetime
class Person:
    def __init__(self,name,surname,birthdate,address,telephone,email):
        self.name=name
        self.surname=surname
        self.birthdate=birthdate
        self.address=address
        self.telephone=telephone
        self.email=email
#instance method
    def age(self):
        today=datetime.date.today()
        age=today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age-=1
        return age

def main():
    person=Person("Minal",
        "Chaudhari",
        datetime.date(1995, 5, 6),
        "jalgaon",
        "1234567",
        "minal@gmail.com"
    )
    print(person.name)
    print(person.surname)
    print(person.address)
    print(person.email)
    print(person.birthdate)
    print(person.age())
    print isinstance(person,Person)

if __name__=='__main__':
    main()