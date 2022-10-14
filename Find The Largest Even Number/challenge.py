def largest_even(list):
 list  = [ x for x in list if x % 2 == 0]
 return -1 if len(list) ==0 else max(list)



