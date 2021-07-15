import gzip
import json
import random

#Selects text body relative to text length and then store that data to easy_text, medium_text or hard_text depending on length of text
def text_selector():
    with gzip.open('examples.json.gz', 'r') as f:
        data = json.load(f)
        
        easy_list = []
        med_list = []
        hard_list = []
        
        for item in data:

            text = item[2]

            if len(text) <= 100:
                easy_list.append(text)
                
            elif len(text) >= 101 and len(text) <= 200:
                med_list.append(text)
                
            else:
                hard_list.append(text)
                
        return easy_list, med_list, hard_list

def random_entr():
    pass

def easy():
    easy_lst = text_selector()
    random_text = random.choice(easy_lst[0]) 
    return random_text

def med():
    med_lst = text_selector()
    random_text = random.choice(med_lst[1]) 
    return random_text

def hard():
    hard_lst = text_selector()
    random_text = random.choice(hard_lst[2]) 
    return random_text