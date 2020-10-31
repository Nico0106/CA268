def rprint(a, b):
    if a < b:
        print(a, end="\n")
        rprint(a + 1, b)
