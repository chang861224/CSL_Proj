import json

def getEntity(term):
    f = open('parseEntity.json')

    array = json.load(f)
    entities = []
    
    for item in array:
        for word in item[term]:
            if word not in entities and word[0] >= 'a' and word[0] <= 'z':
                entities.append(word)

    entities.sort()
    return entities

def getPair(term):
    f = open('parseCombination.json')

    array = json.load(f)
    pairs = []

    for item in array:
        for words in item[term]:
            tag = True
            for word in words:
                if len(word) > 0 and (word[0] < 'a' or word[0] > 'z'):
                    tag = False
            if tag:
                pairs.append(words)

    return pairs

