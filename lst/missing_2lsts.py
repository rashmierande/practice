def missing_2lst(lst1,lst2):
    lst3=[]
    for i in lst1:
        if i not in lst2:
            lst3.append(i)

    return lst3

l1=[1,2,4,6]
l2=[1,2,6]

print(missing_2lst(l1,l2))

def missing(lst1,lst2):
    return set(lst1)^set(lst2)

l1=[1,2,4,6]
l2=[1,2,6,7]

print(missing(l1,l2))

print(set(l1)&set(l2))


# s.symmetric_difference(t)	s ^ t	new set with elements in either s or t but not both
# len(s)	 	number of elements in set s (cardinality)
# x in s	 	test x for membership in s
# x not in s	 	test x for non-membership in s
# s.issubset(t)	s <= t	test whether every element in s is in t
# s.issuperset(t)	s >= t	test whether every element in t is in s
# s.union(t)	s | t	new set with elements from both s and t
# s.intersection(t)	s & t	new set with elements common to s and t
# s.difference(t)	s - t	new set with elements in s but not in t
# s.symmetric_difference(t)	s ^ t	new set with elements in either s or t but not both
# s.copy()	 	new set with a shallow copy of s