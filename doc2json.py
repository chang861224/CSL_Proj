import json

f = open('dataset.txt', 'r')
#w = open('data.json', 'w')
w1 = open('sentence.json', 'w')
w2 = open('cause.json', 'w')
w3 = open('effect.json', 'w')

count = 0
Sentence = []
Cause = []
Effect = []

for i in range(1, 1751):
    A = f.readline().split('\n')[0]
    B = f.readline().split('\n')[0]
    C = f.readline().split('\n')[0]
    D = f.readline().split('\n')[0]
    E = f.readline().split('\n')[0]
    F = f.readline().split('\n')[0]
    f.readline()
    count += 1

    sentence = {'_id': count, 'sentence': B}
    cause = {'_id': count, 'cause': D}
    effect = {'_id': count, 'effect': F}

    Sentence.append(sentence)
    Cause.append(cause)
    Effect.append(effect)

w1.write(json.dumps(Sentence))
w2.write(json.dumps(Cause))
w3.write(json.dumps(Effect))
