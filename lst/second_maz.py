def get_secondMax(lst):
    max,sec=0,0
    for ele in lst:
        if ele>max:
            max,sec=ele,max
        elif ele<max and ele>sec:
            sec=ele
    return sec

print(get_secondMax([3,4,1,5]))


