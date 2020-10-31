import sys

word = sys.argv[1]
a = []
for ch in word:
    a.append(ch)

i = 0
count = 0
while i < len(word):
    count += 1
    i += 1

if count % 2 == 0:
    k = []
    i = count // 2
    while i < count:
        k.append(a[i])
        i += 1
    print(''.join(k))

else:
    j = []
    j.append(word[0])
    j.append(word[-1])
    print(''.join(j))
