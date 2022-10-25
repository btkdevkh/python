# STANDARD INPUT
# radius = input('Enenter the radius of the circle (m): ')
# area = 3.142 * int(radius) ** 2
# print('The area is:', area)

# -------------------------------------------------------

# STRING FORMATTING
# num1 = 3.1515151841
# num2 = 11.232326595
# print(f'num 1 is {num1:.4f} and num 2 is {num2:.4f}')

# -------------------------------------------------------

# IF STATEMENTS
# age = int(input('Enter your age: '))
# if age < 10:
#   print('You are young !')
# elif(age < 18):
#   print('You are teenager !')
# else:
#   print('You are major !')

# -------------------------------------------------------

# FOR LOOPS
# fruits = ['apple', 'orange', 'grape', 'cherry']
# for fruit in fruits:
#   print(fruit)

# for fruit in fruits[1:3]:
#   print(fruit)

# for fruit in fruits:
#   if fruit == 'apple':
#     print(f'{fruit} is like a company brand call APPLE')
#     # break
#   else:
#     print(fruit)

# -------------------------------------------------------

# WHILE LOOPS
# age = 32
# i = 0

# while i < age:
#   if i == 0:
#     i += 1
#     continue
#   if i % 2 == 0:
#     print(i)
#   if i > 20:
#     break
#   i += 1

# -------------------------------------------------------

# RANGES
# for n in range(10):
#   print(n)

# burgers = ['beef', 'chicken', 'veg', 'supreme', 'double']
# for n in range(len(burgers)):
#   print(n, burgers[n])

# for n in range(len(burgers) - 1, -1, -1):
#   print(n, burgers[n])

# -------------------------------------------------------

# FUNCTIONS
# def greet():
#   print('Hello World')

# greet()

# def presentMySelf(name = 'Jimmy'):
#   print(f'Hello, I\'m {name}')

# presentMySelf()

# def area(radius):
#   return 3.142 * int(radius) ** 2

# def vol(area, length):
#   return area * length

# print(vol(area(7), 8))

# -------------------------------------------------------

# DICTIONARIES
# person = {
#   "name": 'Jim',
#   "age": 32
# }
# person['role'] = 'Developer'

# person2 = dict(name="James", age=27, height="6ft")
# print(person2)

# print(person.keys())
# print(person.values())
# print(list(person))
# print(list(person.values()))

# def present(list):
#   for key, val in list.items():
#     print(f'I am {key} amd I am a {val} belt')

# ninjas = {}

# while True:
#   ninjas_name = input('Enter a ninja name: ')
#   ninjas_belt = input('Enter a belt colour: ')
#   ninjas[ninjas_name] = ninjas_belt

#   another = input('Add another ? (y/n) ')

#   if another == 'y':
#     continue
#   else:
#     break

# present(ninjas)

# -------------------------------------------------------

# SORTING & SETS
# def belt_count(dictionary):
#   belts = list(dictionary.values())
#   for belt in set(belts):
#     num = belts.count(belt)
#     print(f'There are {num} {belt} belts')

# ninjas = {}

# while True:
#   ninjas_name = input('Enter a ninja name: ')
#   ninjas_belt = input('Enter a belt colour: ')
#   ninjas[ninjas_name] = ninjas_belt

#   another = input('Add another ? (y/n) ')

#   if another == 'y':
#     continue
#   else:
#     break

# belt_count(ninjas)

# -------------------------------------------------------

# CLASSES
# class Person:
#   # class level attributes
#   theWayOfThinking = 'optimism'

#   # __init__ funtion is a bit like a constructor in JS
#   def __init__(self, firsName, lastName, age):
#     # instance attributes
#     self.firsName = firsName
#     self.lastName = lastName
#     self.age = age

#   # instance method
#   def present(self):
#     return f'Hi, I\'m {self.firsName} and I\'m {self.age} year olds'

#   # class method
#   @classmethod
#   def commons(cls):
#     return f'Their ways of thinking are {cls.theWayOfThinking}'

#   # static method
#   @staticmethod
#   def rythme(workHard = True):
#     if workHard:
#       return f'Yes, they work hard'
#     else:
#       return f'No, they don\'t work hard'

# person1 = Person('BTK', 'KO', 32)
# person2 = Person('KKH', 'KIM', 22)
# # print(person1.firsName)
# # print(person1.lastName)
# # print(person1.age)
# print(person1.present())
# print(person2.present())
# print(Person.commons())
# print(Person.rythme())

# -------------------------------------------------------

# LIST COMPREHENSIONS
# double prize (normal method)
# prizes = [5,10,50,00,1000]

# dbl_prizes = []
# for prize in prizes:
#   dbl_prizes.append(prize * 2)

# # print(dbl_prizes)

# # comprehension method
# dbl_prizes = [prize*2 for prize in prizes]
# # print(dbl_prizes)

# # squaring numbers (normal method)
# nums = [1,2,3,4,5,6,7,8,9,10]
# squared_even_nums = []
# for num in nums:
#   if (num ** 2) % 2 == 0:
#     squared_even_nums.append(num ** 2)

# # print(squared_even_nums)

# # comprehension method
# squared_even_nums = [num ** 2 for num in nums if (num ** 2) % 2 == 0]
# print(squared_even_nums)

# -------------------------------------------------------

# MAPS
# from random import shuffle

# def jumble(word):
#   anagrams = list(word)
#   shuffle(anagrams)
#   return ''.join(anagrams)


# words = ['beetroot', 'carrots', 'potatoes']
# anagrams = []

# for word in words:
#   anagrams.append(jumble(word))
# print(anagrams)

# print(list(map(jumble, words)))
# print([jumble(word) for word in words])

# -------------------------------------------------------

# FILTERS
# grades = ['A','B','F','C','F','A']

# def remove_fails(grade):
#   return grade != 'F'

# print(list(filter(remove_fails, grades)))

# with for method
# filtered_grades = []
# for grade in grades:
#   if grade != 'F':
#     filtered_grades.append(grade)
# print(filtered_grades)

# with comprehension method
# print([grade for grade in grades if grade != 'F'])

# -------------------------------------------------------

# LAMBDAS (anonymous func)
# nums = [1,2,3,4,5,6]
# print(list(map(lambda n: n * n, nums)))

# -------------------------------------------------------

# DECORATORS
# def cough_dec(func):
#   def func_wrapper():
#     # code before funtion
#     print('*cough*')
#     func()
#     # code after function
#     print('*cough*')

#   return func_wrapper

# @cough_dec
# def question():
#   print('can you give me a discount on that ?')

# question()

# -------------------------------------------------------

# READING FILES
# ipsum_file = open('files/ipsum.txt')

# for line in ipsum_file:
#   print(line.rstrip())

# ipsum_file.seek(0)
# lines = ipsum_file.readlines()
# print(lines)

# ipsum_file.seek(50)
# file_text = ipsum_file.read(100)
# print(file_text)

# ipsum_file.close()

# def sequence_filter(line):
#   return '>' not in line

# Don't need to close file with this way
# with open('files/ipsum.txt') as dna_file:
#   lines = dna_file.readlines()
#   print(list(filter(sequence_filter, lines)))

# -------------------------------------------------------

# WRITING FILES
# from asyncore import write


# with open('files/write.txt', 'w') as write_file:
#   write_file.write('Hello World !')

# # junk

# with open('files/write.txt', 'a') as write_file:
#   write_file.write('\nI love you !')

# quotes = [
#   '\nBe yourself; everyone else is already taken.',
#   '\nSo many books, so little time.',
#   '\nA room without books is like a body without a soul.'
# ]

# with open('files/write.txt', 'a') as write_file:
#   write_file.writelines(quotes)

# -------------------------------------------------------

# DOWNLOADING IMAGES
# import urllib.request

# def dl_jpg(url, filepath, filename):
#   fullpath = filepath + filename + '.jpg'
#   urllib.request.urlretrieve(url, fullpath)

# url = input('Enter img URL to download: ')
# file_name = input('Enter file name to save as: ')

# dl_jpg(url, 'images/', file_name)
