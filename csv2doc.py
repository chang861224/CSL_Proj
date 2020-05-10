import re

f = open('fin_pairs.csv', 'r')
w = open('document.txt', 'w')
doc = re.split(r'["\n]', f.read())
count = 0

for d in doc:
    if d != '' and d != '\n' and d != '{' and d != '}' and d != ',' and d != ':' and d != 'sentence':
        count += 1
        w.write('(S){}(E)"\n'.format(d))
