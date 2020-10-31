def sumto(a, b):
    sum = 0
    if a < b:
        sum +=a
        sumto(a+1, b-1)
    return sum
