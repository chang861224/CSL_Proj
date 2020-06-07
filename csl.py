import json

f = open('NTUSD-Fin/NTUSD_Fin_word_v1.0.json')

dataset = json.load(f)

f.close()

array = []

f = open('sentimentWord.json','w')

for data in dataset:
    array.append({"token": data['token'],"market_sentiment": data['market_sentiment']})
    print(data['token'])

f.write(json.dumps(array))
f.close()
