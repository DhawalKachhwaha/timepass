import requests
import re
from bs4 import BeautifulSoup
import spacy
from pandas import *
from spacy.pipeline import EntityRuler

url=input('Enter the URL:')
r = requests.get(url)
pattern = r'"(.*?)"'
matches = re.findall(pattern, r.text)
sentence=" ".join([i for i in matches if len(i)>35 and "https" not in i])

print(sentence)

df=read_csv("words_dataset.csv")
nlp = spacy.load('browser_model')
doc = nlp(sentence)
total=0
nsfw_count=0
for i in doc.ents:
    total+=1
    if i.label_=='NSFW':
        nsfw_count+=1
try:
    if ((nsfw_count/abs(total-nsfw_count))*100)>20:
        print("NSFW:",nsfw_count)
        print("Total:",total)
        print('Block this website.')
    else:
        print("NSFW:",nsfw_count)
        print("Total:",total)
        print('Website safe to surf')
except ZeroDivisionError:
    print("NSFW:",nsfw_count)
    print("Total:",total)
    print('Website safe to surf')
