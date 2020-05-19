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
            if word not in entities and word[0] >= 'a' and word[0] <= 'z':
                entities.append(word)

    entities.sort()
    return entities

def getPair(term):
    #f = open('parseCombination.json', 'r')
    filename = '{}.json'.format(term)
    f = open(filename, 'r')

    lines = f.readlines()
    pairs = []
    count = 0

    for line in lines:
        item = json.loads(line)

        for (i, n) in zip(re.split(r'\(|\)', item[term]), range(1, 100)):
            if n%2 == 0:
                words = [w.lower() for w in i.split(',')]
                words.sort()

                if words not in pairs:
                    tag = True
                    for word in words:
                        if len(word) == 0:
                            tag = False
                        elif word[0] < 'a' or word[0] > 'z':
                            tag = False
                    if tag == True:
                        pairs.append(words)

    return pairs

