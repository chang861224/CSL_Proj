import json

f = open('NTUSD-Fin/NTUSD_Fin_word_v1.0.json')

dataset = json.load(f)

array = []

for data in dataset:
    array.append({"token": data['token'], "dif": data['bull_freq']-data['bear_freq'], "market_sentiment": data['market_sentiment']})
    print(data['token'])

for data in array:
    print(data)
    
print('Total:', len(dataset))
