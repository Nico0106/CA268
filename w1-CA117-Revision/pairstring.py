import sys

word = sys.argv[1]

a = []
for ch in word:
    a.append(ch)

i = 0
while i < len(a):
    try:
        print(a[i] + (a[i + 1]))
    except:
        break
    i = i + 1
