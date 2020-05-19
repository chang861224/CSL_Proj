import json
import re

def getEntity(term):
    #f = open('parseEntity.json', 'r')
    filename = '{}.json'.format(term)
    f = open(filename, 'r')

    lines = f.readlines()
    entities = []
    
    for line in lines:
        item = json.loads(line)
        words = [i.lower() for i in re.split(r'\(|\)', item[term])[0].split() if item != 'exist']
        
        for word in words:
            if word not in entities:
                entities.append(word)

#    entities = entities.sort()

    return entities

