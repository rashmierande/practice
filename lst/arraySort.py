def array_sort(lst):
    for i in range(len(lst)-1,0,-1):
        for n in range(i):
            if lst[n]>lst[n+1]:
                temp=lst[n]
                lst[n]=lst[n+1]
                lst[n+1]=temp
    return lst


print(array_sort([4,5,2,1]))


def array_sort(lst):
    for i in range(0,len(lst)):
        for n in range(i):
            if lst[n]>lst[n+1]:
                temp=lst[n]
                lst[n]=lst[n+1]
                lst[n+1]=temp
    return lst

print(array_sort([4,2,1,9]))