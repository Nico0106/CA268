def set_stuff(a, b):
    U = []
    for word in a:
        U.append(word)
    for word in b:
        U.append(word)
    U = set(U)
    return(U, a.issubset(b), a.issuperset(b))
