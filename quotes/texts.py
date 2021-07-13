import gzip
import json

def read_text():
    #Dictionary that will contain text entries
    with gzip.open('examples.json.gz', 'r') as f:
        data = json.load(f)
    return data

print(read_text())
