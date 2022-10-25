class Person:
  # class level attributes
  theWayOfThinking = 'optimism'

  # __init__ funtion is a bit like a constructor in JS
  def __init__(self, firsName, lastName, age):
    # instance attributes
    self.firsName = firsName
    self.lastName = lastName
    self.age = age

  # instance method
  def present(self):
    return f'Hi, I\'m {self.firsName} and I\'m {self.age} year olds'

  # class method
  @classmethod
  def commons(cls):
    return f'Their ways of thinking are {cls.theWayOfThinking}'

  # static method
  @staticmethod
  def rythme(workHard = True):
    if workHard:
      return f'Yes, they work hard'
    else:
      return f'No, they don\'t work hard'