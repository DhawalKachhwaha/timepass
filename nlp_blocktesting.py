import requests
import re
from bs4 import BeautifulSoup
import spacy
from pandas import *
from spacy.pipeline import EntityRuler

def CheckWebsite(url):
    #Check Count
    total=0
    nsfw_count=0
    #Send Request
    r = requests.get(url)
    nsfw=['Inappropriate Content', 'Gambling and Betting', 'Violence and Gore', 'Drugs', 'Hacking', 'Hate Speech' , 'Social Media and Chatting', 'Firearms and Weapons']
    #Pattern Matching all strings in the HTML content
    pattern = r'"(.*?)"'
    matches = re.findall(pattern, r.text)
    sentence=" ".join([i for i in matches if len(i)>35 and "https" not in i])
    #Load and Use Custom NER Model
    nlp = spacy.load('blocklist_ner')
    doc = nlp(sentence)
    for i in doc.ents:
        total+=1
        if i.label_ in nsfw:
            print(i, i.label_)
            nsfw_count+=1
    try:
        if nsfw_count>total or ((nsfw_count/abs(total))*100)>20:
            print("NSFW:",nsfw_count)
            print("Total:",total)
            return True #True for Blocking the website
        else:
            print("NSFW:",nsfw_count)
            print("Total:",total)
            return False #False for No need of Blocking the website
    except ZeroDivisionError:
        print("NSFW:",nsfw_count)
        print("Total:",total)
        return False

if __name__ == "__main__":
    url=input('Enter the URL:')
    print(CheckWebsite(url))
    
    

'''
##Code for creating a model so you don't waste a whole day figuring it out##
nlp1 = spacy.load("en_core_web_sm")

nlp2 = spacy.blank("en")  # This will be your custom NER model

df = pd.read_csv("words_dataset.csv")  # Columns: 'word', 'cat'

ruler = nlp2.add_pipe("entity_ruler", config={"overwrite_ents": True})

patterns = [{"label": row["cat"], "pattern": row["word"]} for _, row in df.iterrows()]
ruler.add_patterns(patterns)

nlp2.vocab = nlp1.vocab

nlp2.to_disk("blocklist_ner")

'''
