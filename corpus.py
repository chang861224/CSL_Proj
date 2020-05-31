import json

def getEntity(term):
    f = open('parseEntity.json')

    array = json.load(f)
    entities = []
    
    for item in array:
        for word in item[term]:
            if word not in entities and word[0] >= 'a' and word[0] <= 'z' and isLegal(word):
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
            if tag and isLegal(words):
                pairs.append(words)

    return pairs

def text2text(text, term):
    f = open('parseEntity.json')

    array = json.load(f)
    words = []

    for item in array:
        if text in item['cause']:
            for word in item[term]:
                if word not in words:
                    words.append(word)

    return words

def text2pair(text, term):
    f = open('parseCombination.json')

    array = json.load(f)
    pairs = []

    for item in array:
        for pair in item['cause']:
            if text in pair:
                for words in item[term]:
                    if words not in pairs:
                        pairs.append(words)
                break

    return pairs

def isLegal(term):
    stopwords = ['read', 'halt', 'number', 'call']
    if type(term) == str:
        if '.' in term or ',' in term or '?' in term or '&' in term or '\'' in term or '/' in term or '-' in term or term[0] < 'a' or term[0] > 'z' or term in stopwords:
            return False

    if type(term) == list:
        for word in term:
            if '.' in word or ',' in word or '?' in word or '&' in word or '\'' in word or '/' in word or '-' in word or word[0] < 'a' or word[0] > 'z' or word in stopwords:
                return False

    return True

