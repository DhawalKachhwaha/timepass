import requests
from bs4 import BeautifulSoup


r = requests.get('https://www.smith-wesson.com')
soup = BeautifulSoup(r.content, 'html.parser')
s = soup.find('div')
sentence = str(soup.find_all('p'))
import spacy
from pandas import *
from spacy.pipeline import EntityRuler
df=read_csv("words_dataset.csv")
nlp = spacy.load('browser_model')
doc = nlp(sentence)
total=0
nsfw_count=0
for i in doc.ents:
    total+=1
    print(i.ent_,i.label_)
    if i.label_=='NSFW':
        print(i.ent_,i.label_)
        nsfw_count+=1
try:
    if ((nsfw_count/total)*100)>30:
        print('Block this website.')
    else:
        print('Website safe to surf')
except ZeroDivisionError:
    print('Website safe to surf')
    



