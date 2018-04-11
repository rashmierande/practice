def missing_ele(lst):
    start,end=lst[0],lst[-1]
    return sorted(set(range(start,end+1)).difference(lst))


L = [10,11,13,14,15,16,17,18,20]

print(missing_ele(L))

