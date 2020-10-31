def maxi(a, b):
   if a >= b:
      return a
   else:
      return b


def maximum(lst):
    if len(lst) == 1:
        return lst[0]


    return maxi(lst[0], maximum(lst[1:]))
