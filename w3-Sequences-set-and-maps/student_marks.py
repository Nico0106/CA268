def make_map():
    import sys
    d = {}
    for pair in sys.stdin:
        try:
            name, mark = pair.strip().split()
            d[name] = mark
        except:
            break

    return d
