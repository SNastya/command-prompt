spis = []
from operator import itemgetter, attrgetter, methodcaller

with open("words_freq.txt", "r", encoding="utf-8-sig") as f:
    for line in f.readlines():
        line = line.strip().split(' ')
        line[0] = int(line[0])
        spis.append(line)
    

f.close()
print(sorted(spis, key = itemgetter(0) , reverse=True)[:10])
