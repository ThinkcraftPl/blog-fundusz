import nltk
from nltk import ngrams
from collections import defaultdict
import random
import os
full_path = os.path.realpath(__file__)
text=['0','1','2','3','4','5','6','7',' ','9']
with open(os.path.dirname(full_path)+'\\books\\'+'1342-0.txt',  'r', encoding='utf-8-sig') as plik:
  text[0] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'11-0.txt', 'r', encoding = 'utf-8-sig') as plik:
  text[1] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'pg2193.txt', 'r', encoding = 'utf-8-sig') as plik:
  text[2] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'1661-0.txt', 'r', encoding = 'utf-8-sig') as plik:
  text[3] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'1952-0.txt', 'r', encoding = 'utf-8-sig') as plik:
  text[4] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'215-0.txt', 'r', encoding = 'utf-8-sig') as plik:
  text[5] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'84-0.txt', 'r', encoding = 'utf-8-sig') as plik:
  text[6] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'pg1635.txt', 'r', encoding = 'utf-8-sig') as plik:
  text[7] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'pg844.txt', 'r', encoding = 'utf-8-sig') as plik:
  text[9] = plik.read()
text1=text[0].split()
for i in range(1,10):
  text1+=text[i].split()
def unigram():
  unigrams= ngrams(text1, 1)
  print("unigramy:")
  unipolaczenia = []
  unipolaczenia = defaultdict(lambda: defaultdict(int))
  for grams in unigrams:
    slowo=grams[0]
    unipolaczenia["1"][slowo]+=1
  ilosc_wystapien = float(sum(unipolaczenia["1"].values()))
  for slowo in unipolaczenia["1"]:
    unipolaczenia["1"][slowo] /= ilosc_wystapien
  lancuch=[]
  for i in range(100):
    i=i
    try:
      #print("test")
      lancuch.append(random.choices(
          population = list(unipolaczenia["1"].keys()),
          weights = list(unipolaczenia["1"].values()),
          k = 1
      )[0])
    except Exception as e:
      #print(e)
      break
  ' '.join(lancuch)
  #print(lancuch)
  return lancuch
def bigram(start):
  print("bigramy:")
  bigrams= ngrams(text1, 2)
  polaczenia = defaultdict(lambda: defaultdict(int))
  for grams in bigrams:
      #print(grams)
      slowo1=grams[0]
      slowo2=grams[1]
      polaczenia[slowo1][slowo2] += 1
  for slowo1 in polaczenia:
    ilosc_wystapien = float(sum(polaczenia[slowo1].values()))
    for slowo in polaczenia[slowo1]:
      polaczenia[slowo1][slowo] /= ilosc_wystapien
  dlugosc_lancucha=100
  if start == "":
    lancuch=['The']
  else:
    lancuch=start.split(' ')
  for i in range(dlugosc_lancucha):
    i=i
    try:
      lancuch.append(random.choices(
          population = list(polaczenia[lancuch[-1]].keys()),
          weights = list(polaczenia[lancuch[-1]].values()),
          k = 1
      )[0])
    except:
      break
  ' '.join(lancuch)
  return lancuch
def gram3(start):
  polaczenia3 = defaultdict(lambda: defaultdict(int))
  trzgrams= ngrams(text1, 3)
  print("3-gramy:")
  for grams in trzgrams:
    slowo1=grams[0]
    slowo2=grams[1]
    slowo3=grams[2]
    polaczenia3[(slowo1,slowo2)][slowo3] +=1
  for (slowo1, slowo2) in polaczenia3:
    ilosc_wystapien = float(sum(polaczenia3[(slowo1, slowo2)].values()))
    for slowo in polaczenia3[(slowo1, slowo2)]:
      polaczenia3[(slowo1, slowo2)][slowo] /= ilosc_wystapien
  if start == "" or len(start.split(' '))<2:
    lancuch3=['It','was']
  else:
    lancuch3=start.split(' ')
  for i in range(100):
    i=i
    if lancuch3[-1] == '.':
      break
    try:
      lancuch3.append(random.choices(
          population = list(polaczenia3[tuple(lancuch3[-2:])].keys()),
          weights = list(polaczenia3[tuple(lancuch3[-2:])].values()),
          k = 1
      )[0])
    except:
      break
  ' '.join(lancuch3)
  return lancuch3
def gram4(start):
  polaczenia2 = defaultdict(lambda: defaultdict(int))
  czgrams= ngrams(text1, 4)
  print("4-gramy:")
  for grams in czgrams:
      slowo1=grams[0]
      slowo2=grams[1]
      slowo3=grams[2]
      slowo4=grams[3]
      polaczenia2[(slowo1, slowo2, slowo3)][slowo4] += 1
  for (slowo1, slowo2, slowo3) in polaczenia2:
    ilosc_wystapien = float(sum(polaczenia2[(slowo1, slowo2, slowo3)].values()))
    for slowo in polaczenia2[(slowo1, slowo2, slowo3)]:
      polaczenia2[(slowo1, slowo2,slowo3)][slowo] /= ilosc_wystapien
  if start == "" or len(start.split(' '))<3:
    lancuch2=['It','was','a']
  else:
    lancuch2=start.split(' ')
  for i in range(100):
    i=i
    if lancuch2[-1] == '.':
      break
    try:
      lancuch2.append(random.choices(
          population = list(polaczenia2[tuple(lancuch2[-3:])].keys()),
          weights = list(polaczenia2[tuple(lancuch2[-3:])].values()),
          k = 1
      )[0])
    except:
      break
  ' '.join(lancuch2)
  return lancuch2