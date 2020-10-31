def get_counts_dict(list):
    d = {}

    for word in list:
        if len(word) in d:
            d[len(word)] += 1
        else:
            d[len(word)] = 1
    return d
