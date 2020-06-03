import json

f = open('LoughranMcDonald_MasterDictionary_2018.csv', 'r')

lines = f.readlines()
firstline = True

negative = []
positive = []
uncertainty = []
litigious = []

for line in lines:
    if firstline:
        firstline = False
    else:
        string = line.split(',')
        if int(string[7]) > 0:
            negative.append(string[0].lower())
        if int(string[8]) > 0:
            positive.append(string[0].lower())
        if int(string[9]) > 0:
            uncertainty.append(string[0].lower())
        if int(string[10]) > 0:
            litigious.append(string[0].lower())

w = open('sentiment_dict_fin.json', 'w')

w.write(json.dumps({'positive': positive, 'negative': negative, 'uncertainty': uncertainty, 'litigious': litigious}))

w.close()
f.close()
