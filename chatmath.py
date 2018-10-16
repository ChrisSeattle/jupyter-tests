import pandas as pd

with open('chat.txt', 'r') as myfile:
    data=myfile.read().replace('\n', '')
data = data.split(' ')
chatdict = {}
for item in data:
    if item not in chatdict:
        chatdict[item] = 1
    else:
        chatdict[item] += 1

for k, v in chatdict.items():
    print(str(k) + ':' + str(v))

s = pd.Series(d, name='DateValue')