import numpy as np

from redo import *
import datetime as dt
import pandas as pd

tweet = pd.read_csv("tweet_covid.csv")
df = tweet
corpus = df['tweet']
corpus_clean = corpus.apply(nlp_pipeline)

from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

polarity = []
for tweet in corpus_clean:
  polarity.append(TextBlob(tweet,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer()).sentiment[0])
  polarity.append(TextBlob(tweet,pos_tagger=PatternTagger(),analyzer=PatternAnalyzer()).sentiment[1])
import matplotlib.pyplot as plt
#plt.plot(polarity)

group = lambda liste, size : [liste[i:i+size] for i in range(0, len(liste), size)]

polarity_par_paquet = group(polarity,1000)

liste_moyennes = []
for l in polarity_par_paquet :
  liste_moyennes.append(np.mean(l))

plt.plot(liste_moyennes)
   
print(liste_moyennes)
plt.show()

plt.savefig('foo.png')
plt.savefig('foo.pdf')

