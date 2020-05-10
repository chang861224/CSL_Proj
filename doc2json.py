import json

f = open('dataset.txt', 'r')
#w = open('col_1.json', 'w')
#w = open('col_2.json', 'w')
#w = open('col_3.json', 'w')
w = open('data.json', 'w')

count = 0

for i in range(1, 1751):
#   f.readline()
#   f.readline()
#   f.readline()
#   f.readline()

    count += 1
    
    A = f.readline().split('\n')[0]
    B = f.readline().split('\n')[0]
    C = f.readline().split('\n')[0]
    D = f.readline().split('\n')[0]
    E = f.readline().split('\n')[0]
    F = f.readline().split('\n')[0]

    print('{"_id": ' + str(count) + ', "col_A": "' + A + '", "col_B": "' + B + '", "col_C": "' + C
            + '", "col_D": "' + D + '", "col_E": "' + E + '", "col_F": "' + F + '"}\n')
    w.write('{"_id": ' + str(count) + ', "col_A": "' + A + '", "col_B": "' + B + '", "col_C": "' + C
            + '", "col_D": "' + D + '", "col_E": "' + E + '", "col_F": "' + F + '"}\n')

#   f.readline()
#   f.readline()
#   f.readline()
#   f.readline()
    f.readline()
