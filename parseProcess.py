import re
import json

f1 = open('reason.json', 'r')
f2 = open('result.json', 'r')
f3 = open('sentence.json', 'r')
w = open('parse.json', 'w')

for count in range(1, 1751):
    reason = f1.readline()
    line1 = json.loads(reason)

    result = f2.readline()
    line2 = json.loads(result)

    sentence = f3.readline()
    line3 = json.loads(sentence)

    stringList1 = []
    stringList2 = []
    stringList3 = []

    for (i, n) in zip(re.split(r'\(|\)', line1['reason']), range(1, 100)):
        if n%2 == 0:
            stringList1.append(i.split(','))

    for (i, n) in zip(re.split(r'\(|\)', line2['result']), range(1, 100)):
        if n%2 == 0:
            stringList2.append(i.split(','))

    for (i, n) in zip(re.split(r'\(|\)', line3['sentence']), range(1, 100)):
        if n%2 == 0:
            stringList3.append(i.split(','))

    w.write('{"_id": ' + str(count) + ', "cause": ' + str(stringList1) + ', "effect": ' + str(stringList2) + ', "sentence": ' + str(stringList3) + '}\n')
    print('Item {} .... DONE!'.format(count))
