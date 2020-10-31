import sys

students = sys.argv[1]
delinquints = sys.argv[2]

with open(students) as s:
    data = s.readlines()
    nos = []
    for word in data:
        word = word.strip()
        nos.append(word)
#______________________________________________________
with open(delinquints) as d:
    data = d.readlines()
    nod = []
    for word in data:
        word = word.strip()
        nod.append(word)
#______________________________________________________
both = []

for name in nos:
    if name in nod:
        both.append(name)
#______________________________________________________

both = sorted(both)
i = 1
for name in both:
    print(("{}. {}").format(i, name))
    i += 1
