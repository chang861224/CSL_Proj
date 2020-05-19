import re
import json

f1 = open('cause.json')
f2 = open('effect.json')
f3 = open('sentence.json')
w = open('parseEntity.json', 'w')

Cause = json.load(f1)
Effect = json.load(f2)
Sentence = json.load(f3)
List = []

for (count, c, e, s) in zip(range(1, 1751), Cause, Effect, Sentence):
    cause = [item.lower() for item in re.split(r'\(|\)', c['cause'])[0].split() if item != 'exist']
    cause.pop(0)
    effect = [item.lower() for item in re.split(r'\(|\)', e['effect'])[0].split() if item != 'exist']
    effect.pop(0)
    sentence = [item.lower() for item in re.split(r'\(|\)', s['sentence'])[0].split() if item != 'exist']
    sentence.pop(0)
    item = {'_id': count, 'cause': cause, 'effect': effect, 'sentence': sentence}
    List.append(item)
    print('Item {} .... DONE!'.format(count))

w.write(json.dumps(List))
print('Process DONE!!')

