import json
import nltk
import corpus


# Sentiment Word List in Finance

f = open('sentimentWords.json')
tokens = json.load(f)
f.close()

sentimentWords = {'positive': [], 'negative': [], 'uncertainty': []}

for token in tokens:
    if token['market_sentiment'] > 0.1:
        sentimentWords['positive'].append(token['token'])
        print(token['token'], token['market_sentiment'], 'DONE!!')
    elif token['market_sentiment'] < -0.1:
        sentimentWords['negative'].append(token['token'])
        print(token['token'], token['market_sentiment'], 'DONE!!')
    else:
        sentimentWords['uncertainty'].append(token['token'])
        print(token['token'], token['market_sentiment'], 'DONE!!')




# Dataset Processing

f = open('parseCombination.json')

dataset = json.load(f)
verb = ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']
noun = ['FW', 'NN', 'NNS', 'NNP', 'NNPS']
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
Outcome = {'positive': [], 'negative': [], 'uncertainty': [], 'unknown': []}
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

        if pair[0] in sentimentWords['positive']:
            if pair[0] not in Outcome['positive']:
                Outcome['positive'].append(pair[0])
        elif pair[0] in sentimentWords['negative']:
            if pair[0] not in Outcome['negative']:
                Outcome['negative'].append(pair[0])
        elif pair[0] in sentimentWords['uncertainty']:
            if pair[0] not in Outcome['uncertainty']:
                Outcome['uncertainty'].append(pair[0])
        else:
            if pair[0] not in Outcome['unknown']:
                Outcome['unknown'].append(pair[0])
    
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

for item in Outcome['positive']:
    w.write('influence(positive, X) :- {}(X).\n'.format(item))
    print('influence(positive, X) :- {}(X).\n'.format(item))

for item in Outcome['negative']:
    w.write('influence(negative, X) :- {}(X).\n'.format(item))
    print('influence(negative, X) :- {}(X).\n'.format(item))

for item in Outcome['uncertainty']:
    w.write('influence(uncertainty, X) :- {}(X).\n'.format(item))
    print('influence(uncertainty, X) :- {}(X).\n'.format(item))

for item in Outcome['unknown']:
    w.write('influence(unknown, X) :- {}(X).\n'.format(item))
    print('influence(unknown, X) :- {}(X).\n'.format(item))

w.write('\n')

for item in KB:
    w.write('occur(A, B, C, D, E) :- {}(A), {}(B), {}(C), {}(D), influence(E, C).\n'.format(item['Cause'][0], item['Cause'][1], item['Effect'][0], item['Effect'][1]))
    print('occur(A, B, C, D, E) :- {}(A), {}(B), {}(C), {}(D), influence(E, C).'.format(item['Cause'][0], item['Cause'][1], item['Effect'][0], item['Effect'][1]))

w.write('\n')

# Occurence Function
w.write('occur([FirstA, FirstB | Rest], X, Y, E) :- occur(FirstA, FirstB, X, Y, E), occur(Rest, X, Y, E).\n')
w.write('occur([], _, _, _).\n')

# Reverse Function
w.write('outcome(A, B, E, C, D) :- occur(C, D, A, B, E).\n')
w.write('outcome([FirstA, FirstB | Rest], E, X, Y) :- outcome(FirstA, FirstB, E, X, Y), outcome(Rest, E, X, Y).\n')
w.write('outcome([], _, _, _).\n')

# Files Close
w.close()

