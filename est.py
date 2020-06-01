import json
import nltk
import corpus

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
            #if len(pair) == 2 and len(pair[1]) > 0 and nltk.pos_tag(nltk.word_tokenize(pair[1]))[0][1] in noun and pair[1][0] >= 'a' and pair[1][0] <= 'z':
            if len(pair) == 2 and len(pair[1]) > 0 and corpus.isLegal(pair) and nltk.pos_tag(nltk.word_tokenize(pair[1]))[0][1] in noun:
                if pair not in Cause:
                    print(pair)
                    Cause.append(pair)

    for pair in effect:
        token = nltk.word_tokenize(pair[0])
        if len(nltk.pos_tag(token)) > 0 and nltk.pos_tag(token)[0][1] in verb:
            #if len(pair) == 2 and len(pair[1]) > 0 and nltk.pos_tag(nltk.word_tokenize(pair[1]))[0][1] in noun and pair[1][0] >= 'a' and pair[1][0] <= 'z':
            if len(pair) == 2 and len(pair[1]) > 0 and corpus.isLegal(pair) and nltk.pos_tag(nltk.word_tokenize(pair[1]))[0][1] in noun:
                if pair not in Effect:
                    print(pair)
                    Effect.append(pair)
    """
    for pair in sentence:
        token = nltk.word_tokenize(pair[0])
        if len(nltk.pos_tag(token)) > 0 and nltk.pos_tag(token)[0][1] in verb:
            if len(pair) > 1 and len(pair[1]) > 0 and nltk.pos_tag(nltk.word_tokenize(pair[1]))[0][1] in noun and pair[1][0] >= 'a' and pair[1][0] <= 'z':
                if pair not in Sentence:
                    print(pair)
                    Sentence.append(pair)
    """
    #List.append({'_id': data['_id'], 'Cause': Cause, 'Effect': Effect, 'Sentence': Sentence})
    List.append({'_id': data['_id'], 'Cause': Cause, 'Effect': Effect})

for item in List:
    print('----------')
    print('ID:', item['_id'])
    print('Cause:', item['Cause'])
    print('Effect:', item['Effect'])
    #print('Sentence:', item['Sentence'])
    print('----------')



Noun = []
Verb = []
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
    for x in cause:
        for y in effect:
            KB.append({'Cause': x, 'Effect': y})




############################
##                        ##
##  Write Knowledge Base  ##
##                        ##
############################

w = open('KnowledgeBase.pl', 'w')

for item in Noun:
    w.write('{}({}).\n'.format(item, item))
    print('{}({}).'.format(item, item))

w.write('\n')

for item in Verb:
    w.write('{}({}).\n'.format(item, item))
    print('{}({}).'.format(item, item))

w.write('\n')

for item in KB:
    w.write('occur(A, B, C, D) :- {}(A), {}(B), {}(C), {}(D).\n'.format(item['Cause'][0], item['Cause'][1], item['Effect'][0], item['Effect'][1]))
    print('occur(A, B, C, D) :- {}(A), {}(B), {}(C), {}(D).'.format(item['Cause'][0], item['Cause'][1], item['Effect'][0], item['Effect'][1]))

w.write('\n')

# Occurence Function
w.write('occur([FirstA, FirstB | Rest], X, Y) :- occur(FirstA, FirstB, X, Y), occur(Rest, X, Y).\n')
w.write('occur([], _, _).\n')

# Reverse Function
w.write('reverse(A, B, C, D) :- occur(C, D, A, B).\n')
w.write('reverse([FirstA, FirstB | Rest], X, Y) :- reverse(FirstA, FirstB, X, Y), reverse(Rest, X, Y).\n')
w.write('reverse([], _, _).\n')

# Files Close
f.close()
w.close()

