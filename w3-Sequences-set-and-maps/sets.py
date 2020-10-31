def set_intersection(set1, set2):
    a = []
    for word in set1:
        if word in set2:
                a.append(word)
    return a
