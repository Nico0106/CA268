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

def main():
    student = make_map() # Call the student function
    print(type(student)) # check the type ... should be a map (or in python, dict)
    names = student.keys()   # get all names
    for name in sorted(names): # sort the names
        print(name + " has mark " + student[name]) # print the names and marks

if __name__ == "__main__":
    main()
