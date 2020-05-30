import tensorflow as tf
from pprint import pprint
import numpy as np
import numpy
import os
import re
full_path = os.path.realpath(__file__)
texttab=['0','1','2','3','4','5','6','7','','9']
with open(os.path.dirname(full_path)+'\\books\\'+'1342-0.txt',  'r', encoding='utf-8-sig') as plik:
  texttab[0] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'11-0.txt', 'r', encoding = 'utf-8-sig') as plik:
  texttab[1] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'pg2193.txt', 'r', encoding = 'utf-8-sig') as plik:
  texttab[2] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'1661-0.txt', 'r', encoding = 'utf-8-sig') as plik:
  texttab[3] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'1952-0.txt', 'r', encoding = 'utf-8-sig') as plik:
  texttab[4] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'215-0.txt', 'r', encoding = 'utf-8-sig') as plik:
  texttab[5] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'84-0.txt', 'r', encoding = 'utf-8-sig') as plik:
  texttab[6] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'pg1635.txt', 'r', encoding = 'utf-8-sig') as plik:
  texttab[7] = plik.read()
with open(os.path.dirname(full_path)+'\\books\\'+'pg844.txt', 'r', encoding = 'utf-8-sig') as plik:
  texttab[9] = plik.read()
text=texttab[0].split()
for i in range(1,10):
  text+=texttab[i].split()
text=' '.join(text)
text = text.lower()
text = re.sub(chr(10), '', text)
alfabet = sorted(set(text))
alfabet[:10]
mapowanie = dict((znak, indeks) for indeks, znak in enumerate(alfabet))
odwrotne_mapowanie = np.array(alfabet)
for key in list(mapowanie.keys())[:10]:
  print(key, ': ', mapowanie[key], ': ', ord(key))
print()
print(' '.join(odwrotne_mapowanie[:10]))
tekst = np.array([mapowanie[litera] for litera in text])
print(len(tekst))
print(len(text))
for litera, zakodowana_litera in zip(text[:20], tekst[:20]):
  print(litera, zakodowana_litera)
dlugosc_sekwencji = 100
dataset = tf.data.Dataset.from_tensor_slices(tekst)
for element in dataset.take(7):
  print(element, ': ', odwrotne_mapowanie[element])
sekwencje = dataset.batch(dlugosc_sekwencji + 1, drop_remainder=True)
for element in sekwencje.take(3):
  for znak in element:
    print(odwrotne_mapowanie[znak], end='')
  print('\n\n')
dataset = sekwencje.map(lambda x: (x[:-1], x[1:]))
for input_tekst, target_tekst in dataset.take(3):
  for znak in input_tekst:
    print(odwrotne_mapowanie[znak], end='')
  print()
  for znak in target_tekst:
    print(odwrotne_mapowanie[znak], end='')
  print('\n\n')
dataset = dataset.shuffle(10000)
dataset = dataset.batch(64, drop_remainder=True)
dlugosc_alfabetu = len(alfabet)
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(dlugosc_alfabetu, 
                             256, 
                             batch_input_shape=[64, None]))
model.add(tf.keras.layers.LSTM(1024, 
                              return_sequences=True, 
                              stateful=True, 
                              recurrent_initializer='glorot_uniform',
                              activation='tanh'))
model.add(tf.keras.layers.Dense(dlugosc_alfabetu))
model.summary()
model.compile(optimizer='adam', 
              loss=(
                  lambda labels, logits: 
                  tf.keras.losses.sparse_categorical_crossentropy(
                      labels, 
                      logits, 
                      from_logits=True
                      )
                  )
              )
new_checkpoint_dir = os.path.dirname(full_path)+'\\checkpoints\\'
checkpoint_prefix = os.path.join(new_checkpoint_dir, "ckpt_{epoch}")
checkpoint_callback=tf.keras.callbacks.ModelCheckpoint(
    filepath=checkpoint_prefix,
    save_weights_only=True, 
    save_best_only=False
)
os.chdir(new_checkpoint_dir)
model.fit(dataset, epochs=100, callbacks=[checkpoint_callback])