def get_ThirdMax(lst):
    first,second,third=0,0,0

    for ele in lst:
        if ele>first:
            first,second,third=ele,first,second

        elif ele<first and ele>second:
            second,third=ele,second
        elif ele!=first and ele!=second and ele>third:
            third=ele
    return third

print(get_ThirdMax([1,6,2,3,4,9]))