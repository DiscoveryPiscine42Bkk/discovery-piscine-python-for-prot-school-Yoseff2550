import heapq

num = [2, 8, 9, 48, 8, 22, -12, 2]
plusnum = [x + 2 for x in num]
greatpnum = heapq.nlargest(5, plusnum)
list_great_pnums = [x for x in plusnum if x in greatpnum]
print(list_great_pnums)