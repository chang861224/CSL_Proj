import re
import json

f1 = open('cause.json')
f2 = open('effect.json')
f3 = open('sentence.json')
w = open('parseCombination.json', 'w')

Cause = json.load(f1)
Effect = json.load(f2)
Sentence = json.load(f3)
List = []

for (count, c, e, s) in zip(range(1, 1751), Cause, Effect, Sentence):
    cause = []
    effect = []
    sentence = []

    for (i, n) in zip(re.split(r'\(|\)', c['cause']), range(1, 100)):
        if n%2 == 0:
            compose = [item.lower() for item in i.split(',')]
            compose.sort()
            cause.append(compose)

    for (i, n) in zip(re.split(r'\(|\)', e['effect']), range(1, 100)):
        if n%2 == 0:
            compose = [item.lower() for item in i.split(',')]
            compose.sort()
            effect.append(compose)

    for (i, n) in zip(re.split(r'\(|\)', s['sentence']), range(1, 100)):
        if n%2 == 0:
            compose = [item.lower() for item in i.split(',')]
            compose.sort()
            sentence.append(compose)

    item = {'_id': count, 'cause': cause, 'effect': effect, 'sentence': sentence}
    List.append(item)
    print('Item {} .... DONE!'.format(count))
    
w.write(json.dumps(List))
print('Process DONE!!')
