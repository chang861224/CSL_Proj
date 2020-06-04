import json
import nltk
import corpus


# Sentiment Word List in Finance

f = open('sentiment_dict_fin.json')
sentimentDict = json.load(f)
f.close()




# Dataset Processing

f = open('parseCombination.json')

dataset = json.load(f)
verb = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
noun = ['FW', 'NN', 'NNS', 'NNP', 'NNPS']
ad = ['JJ', 'JJR', 'JJS', 'RB', 'RBR', 'RBS']
List = []

for data in dataset:
    cause = data['cause']
    effect = data['effect']
    sentence = data['sentence']
    Cause = []
    Effect = []
    Sentence = []

    for pair in cause:
        token = nltk.word_tokenize(pair[0])
        if len(nltk.pos_tag(token)) > 0 and nltk.pos_tag(token)[0][1] in verb:
            if len(pair) == 2 and len(pair[1]) > 0 and corpus.isLegal(pair) and nltk.pos_tag(nltk.word_tokenize(pair[1]))[0][1] in noun:
                if pair not in Cause:
                    print(pair)
                    Cause.append(pair)

    for pair in effect:
        token = nltk.word_tokenize(pair[0])
        if len(nltk.pos_tag(token)) > 0 and nltk.pos_tag(token)[0][1] in verb:
            if len(pair) == 2 and len(pair[1]) > 0 and corpus.isLegal(pair) and nltk.pos_tag(nltk.word_tokenize(pair[1]))[0][1] in noun:
                if pair not in Effect:
                    print(pair)
                    Effect.append(pair)
    
    List.append({'_id': data['_id'], 'Cause': Cause, 'Effect': Effect})

Noun = []
Verb = []
Effect = {'positive': [], 'negative': [], 'uncertainty': [], 'unknown': []}
KB = []

for item in List:
    cause = []
    effect = []
    
    for pair in item['Cause']:
        if pair[0] not in Verb:
            Verb.append(pair[0])
        if pair[1] not in Noun:
            Noun.append(pair[1])
        cause.append(pair)
    
    for pair in item['Effect']:
        if pair[0] not in Verb:
            Verb.append(pair[0])
        if pair[1] not in Noun:
            Noun.append(pair[1])
        effect.append(pair)

        if pair[0] in sentimentDict['positive'] and pair[0] not in Effect['positive']:
            Effect['positive'].append(pair[0])
        elif pair[0] in sentimentDict['negative'] and pair[0] not in Effect['negative']:
            Effect['negative'].append(pair[0])
        elif pair[0] in sentimentDict['uncertainty'] and pair[0] not in Effect['uncertainty']:
            Effect['uncertainty'].append(pair[0])
        else:
            if pair[0] not in Effect['unknown']:
                Effect['unknown'].append(pair[0])
    
    for x in cause:
        for y in effect:
            KB.append({'Cause': x, 'Effect': y})

f.close()




# Write Knowledge Base

w = open('KnowledgeBase.pl', 'w')

for item in Noun:
    w.write('{}({}).\n'.format(item, item))
    print('{}({}).'.format(item, item))

w.write('\n')

for item in Verb:
    w.write('{}({}).\n'.format(item, item))
    print('{}({}).'.format(item, item))

w.write('\n')

for item in Effect['positive']:
    w.write('effect(positive, X) :- {}(X).\n'.format(item))
    print('effect(positive, X) :- {}(X).\n'.format(item))

for item in Effect['negative']:
    w.write('effect(negative, X) :- {}(X).\n'.format(item))
    print('effect(negative, X) :- {}(X).\n'.format(item))

for item in Effect['uncertainty']:
    w.write('effect(unceratinty, X) :- {}(X).\n'.format(item))
    print('effect(uncertainty, X) :- {}(X).\n'.format(item))

for item in Effect['unknown']:
    w.write('effect(unknown, X) :- {}(X).\n'.format(item))
    print('effect(unknown, X) :- {}(X).\n'.format(item))

w.write('\n')

for item in KB:
    w.write('occur(A, B, C, D, E) :- {}(A), {}(B), {}(C), {}(D), effect(E, C).\n'.format(item['Cause'][0], item['Cause'][1], item['Effect'][0], item['Effect'][1]))
    print('occur(A, B, C, D, E) :- {}(A), {}(B), {}(C), {}(D), effect(E, C).'.format(item['Cause'][0], item['Cause'][1], item['Effect'][0], item['Effect'][1]))

w.write('\n')

# Occurence Function
w.write('occur([FirstA, FirstB | Rest], X, Y, E) :- occur(FirstA, FirstB, X, Y, E), occur(Rest, X, Y, E).\n')
w.write('occur([], _, _, _).\n')

# Reverse Function
w.write('reverse(A, B, C, D) :- occur(C, D, A, B, _).\n')
w.write('reverse([FirstA, FirstB | Rest], X, Y) :- reverse(FirstA, FirstB, X, Y), reverse(Rest, X, Y).\n')
w.write('reverse([], _, _).\n')

# Files Close
w.close()

