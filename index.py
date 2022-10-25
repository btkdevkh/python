from person.person import Person
from person.calc import birthday

person1 = Person('BTK', 'KO', 32)
person2 = Person('KKH', 'KIM', 22)
# print(person1.firsName)
# print(person1.lastName)
# print(person1.age)
print(person1.present())
print(person2.present())
print(Person.commons())
print(Person.rythme())

print(birthday(2022, 2000))
print(birthday(2022, 1990))
