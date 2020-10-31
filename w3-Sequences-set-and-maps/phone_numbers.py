d = {}
s = input("Enter a name and number, or a name and ? to query (!! to exit)\n")
if s == '!!':
    print('Bye')
else:
    s = s.strip().split()
    while s[0] != '!!':
        d[s[0]] = s[1]
        s = input()
        s = s.strip().split()
        try:
            if s[1] == '?':
                try:
                    print(('{} has number {}').format(s[0], d[s[0]]))
                except:
                    print(('Sorry, there is no {}').format(s[0]))
        except:
            if s[0] == '!!':
                print('Bye')
