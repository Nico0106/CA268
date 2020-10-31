def get_evenodd_list():
    s = int(input())
    list = []
    while s != -1:
        list.append(s)
        s = int(input())
    odd = []
    even = []
    for n in list:
        if int(n) % 2 == 0:
            even.append(n)
        else:
            odd.append(n)

    return odd, even
