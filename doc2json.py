import json

f = open('dataset.txt', 'r')
#w = open('col_1.json', 'w')
#w = open('col_2.json', 'w')
w = open('col_3.json', 'w')

count = 0

for i in range(1, 1751):
    f.readline()
    f.readline()
    f.readline()
    f.readline()

    count += 1
    
    item1 = f.readline().split('\n')[0]
    item2 = f.readline().split('\n')[0]

    print('{"_id": ' + str(count) + ', "item1": "' + item1 + '", "item2": "' + item2 + '"}\n')
    w.write('{"_id": ' + str(count) + ', "item1": "' + item1 + '", "item2": "' + item2 + '"}\n')

#   f.readline()
#   f.readline()
#   f.readline()
#   f.readline()
    f.readline()
