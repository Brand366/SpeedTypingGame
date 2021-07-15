import gzip
import json
import random

#Selects text body relative to text length and then store that data to easy_text, medium_text or hard_text depending on length of text
'''def text_selector():
    with gzip.open('examples.json.gz', 'r') as f:
        data = json.load(f)
        #sorted_data = sorted(data, key=lambda x: [2])
    easy_text = []
    med_text = []
    hard_text = []
    random_entry = random.choice(data)
    random_text = random_entry[2]


    while not (60 < len(random_text) <= 100):
        yield easy_text.append(random_text)

        if len(random_text) <= 200 and len(random_text) > 101:
            yield medium_text.append(random_text)
            
        else:
            yield hard_text.append(random_text)'''




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

def random_entry():
    pass

def easy():
    random_entry = text_selector()
    random_text = random.choice(random_entry[0]) 
    return random_text

def med():
    random_entry = text_selector()
    random_text = random.choice(random_entry[1]) 
    return random_text

def hard():
    random_entry = text_selector()
    random_text = random.choice(random_entry[2]) 
    return random_text



'''def text_selector():
    with gzip.open('examples.json.gz', 'r') as f:
        data = json.load(f)
        #sorted_data = sorted(data, key=lambda x: [2])
        easy_text = ""
        med_text = ""
        hard_text = ""
        random_text = ""

        while not (60 < len(random_text) <= 100):
            random_entry = random.choice(data)
            random_text = random_entry[2]

            return easy_text.join(random_text)

            if len(random_text) <= 200 and len(random_text) > 101:
                return medium_text.join(random_text)

            else:
                return hard_text.join(random_text)

print(text_selector())'''