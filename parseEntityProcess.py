import re
import json

f1 = open('reason.json', 'r')
f2 = open('result.json', 'r')
f3 = open('sentence.json', 'r')
w = open('parseEntity.json', 'w')

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

    stringList1 = [item.lower() for item in re.split(r'\(|\)', line1['reason'])[0].split() if item != 'exist']
    stringList1.pop(0)
    stringList1 = list(dict.fromkeys(stringList1))
    stringList1.sort()

    stringList2 = [item.lower() for item in re.split(r'\(|\)', line2['result'])[0].split() if item != 'exist']
    stringList2.pop(0)
    stringList2 = list(dict.fromkeys(stringList1))
    stringList2.sort()

    stringList3 = [item.lower() for item in re.split(r'\(|\)', line3['sentence'])[0].split() if item != 'exist']
    stringList3.pop(0)
    stringList3 = list(dict.fromkeys(stringList1))
    stringList3.sort()

    w.write('{"_id": ' + str(count) + ', "cause": ' + str(stringList1) + ', "effect": ' + str(stringList2) + ', "sentence": ' + str(stringList3) + '}\n')
    print('Item {} .... DONE!'.format(count))

