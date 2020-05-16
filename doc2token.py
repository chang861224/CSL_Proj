import json
from nltk.corpus import stopwords

stops = stopwords.words('english')
f = open('data.json', 'r')
w = open('token.json', 'w')

lines = f.readlines()

for line in lines:
    item = json.loads(line)
#print(item['col_A'])

    wordA = []
    token = item['col_A'].split(' ')
    for word in token:
        if word not in stops:
            wordA.append(word)
    
    wordB = []
    token = item['col_B'].split(' ')
    for word in token:
        if word not in stops:
            wordB.append(word)

    wordC = []
    token = item['col_C'].split(' ')
    for word in token:
        if word not in stops:
            wordC.append(word)

    wordD = []
    token = item['col_D'].split(' ')
    for word in token:
        if word not in stops:
            wordD.append(word)

    wordE = []
    token = item['col_E'].split(' ')
    for word in token:
        if word not in stops:
            wordE.append(word)

    wordF = []
    token = item['col_F'].split(' ')
    for word in token:
        if word not in stops:
            wordF.append(word)

    w.write('{"_id": ' + str(item['_id']) + ', "col_A": ' + str(wordA) + ', "col_B": ' + str(wordB) + ', "col_C": ' + str(wordC) +
            ', "col_D": ' + str(wordD) + ', "col_E": ' + str(wordE) + ', "col_F": ' + str(wordF) + '}\n')
    print(item['_id'])
