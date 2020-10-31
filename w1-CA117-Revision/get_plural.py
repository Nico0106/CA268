def get_plural(noun):
    a = []
    vowels = 'aeiou'
    for ch in noun:
        a.append(ch)
    if a[-1] == 'o' or a[-2] == 'c' and a[-1] == 'h' or a[-2] == 's' and a[-1] == 'h' or  a[-1] == 'x' or a[-1] == 's' or a[-1] == 'z':
        a.append('es')
    elif a[-1] == 'y':
        if a[-2] in vowels:
            a.append('s')
        else:
            a.pop()
            a.append('ies')
    elif a[-1] == 'f':
        a.pop()
        a.append('ves')
    elif a[-2] == 'f' and a[-1] == 'e':
        a.pop()
        a.pop()
        a.append('ves')
    else:
        a.append('s')
    plural = ''.join(a)
    return plural
