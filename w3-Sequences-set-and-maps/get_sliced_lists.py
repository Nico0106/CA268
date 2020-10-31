def get_sliced_lists(list):

    abl = []
    minfl = []
    reversed = []

    i = 0
    while i < len(list) - 1:
        abl.append(list[i])
        i += 1

    i = 1
    while i < len(list) -1:
        minfl.append(list[i])
        i += 1

    i = 0
    j = -1
    while i < len(list) / 2:
        tmp = list[i]
        list[i] = list[j]
        list[j] = tmp
        i += 1
        j -= 1

    for n in list:
        reversed.append(n)

    return abl, minfl, reversed

def main():
    # read the list from stdin
    nums = []
    num = int(input())
    while num != -1:
        nums.append(num)
        num = int(input())

    # call the student's function with the list of numbers and ...
    lists = get_sliced_lists(nums)
    # ... print the result
    for lst in lists:
        print(lst)

if __name__ == "__main__":
    main()
