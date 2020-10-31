def get_odd_list():
    s = int(input())
    list = []
    while s != -1:
        list.append(s)
        s = int(input())
    odds = []
    for n in list:
        if n % 2 != 0:
            odds.append(n)
    return odds

def main():
    # call the get_odd_list function and print the result
    odds = get_odd_list()
    print(odds)

if __name__ == "__main__":
    main()
