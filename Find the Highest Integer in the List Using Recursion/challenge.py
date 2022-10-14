def find_highest(lst):
 if len(lst) > 1:
         lst.remove(min(lst))
         print(lst)
         return find_highest(lst)
 else:
          return lst[0]

print(find_highest([12]))          


        