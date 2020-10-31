s = input()
list = []
while s != '-1':
    list.append(s)
    s = input()

a = []
i = 1
while i < len(list):
    seen = list[:i]
    if list[i] in seen:
        a.append(list[i])
    i += 1

print("Enter numbers (-1 to end):", " ".join(a))
