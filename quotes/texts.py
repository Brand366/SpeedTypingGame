import gzip
import json
import random

#Selects text body relative to text length and then store that data to easy_text, medium_text or hard_text depending on length of text
def text_selector():
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

print(read_text())


