import gzip
import json

def read_text(examples.json.gz):
    #Dictionary that will contain text entries
    dictionary = {}
    with gzip.open('examples.json.gz', 'r') as f:
        data = json.load(f)
    return data

print(read_text())