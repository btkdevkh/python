from random import randint

jim_word = [
  'Adoo', 'Bdhjsd', 'Cggk', 'Dhhkkht', 'Ejgkf'
]

def jimrize(word):
  random_pos = randint(0, len(jim_word) - 1)
  return f'{word} {jim_word[random_pos]}'

paragraphs = int(input('How many paragraphs of jim ipsum: '))

with open('ipsum.txt') as ipsum_original:
  items = ipsum_original.read().split()

  for n in range(paragraphs):
    jim_text = list(map(jimrize, items))
    with open('ipsum_jim.txt', 'a') as ipsum_jim:
      ipsum_jim.write(' '.join(jim_text) + '\n\n')

