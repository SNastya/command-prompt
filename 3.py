a=[0]*(ord('я')-ord('а')+2)
with open('words_freq.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():
        b=line.split()
        if ord(b[1][0].lower())<=ord('я') and ord(b[1][0].lower())>=ord('а'):
            a[ord(b[1][0].lower())-ord('а')]+=int(b[0])
ma=max(a)

for i in range(len(a)):
    if a[i]==ma:
        print(chr(ord('а')+i), a[i])
        exit()