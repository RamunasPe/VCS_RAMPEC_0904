HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

import random

lygis = input('pasirinkite lygi: ')
zodziu_sarasas = []
while lygis <= 2 or lygis >= 9:
    lygis = input('lygis netinkamas, pasirinkite didesni/mazesni')
print lygis
failo_objektas = open('zodziu_sarasas.txt', 'r')
for zodis in failo_objektas.readlines():
    zodzio_ilgis = len(zodis)
   # print zodzio_ilgis
    if int(lygis) >= int(zodzio_ilgis):
        zodziu_sarasas.append(zodis.replace('\n', ""))
#print zodzio_ilgis #tikrinimui

random_index = random.randint(0, len(zodziu_sarasas))
spejimas = zodziu_sarasas[random_index]
print spejimas


#a = input ('ivesk raide: ')
#if a ==