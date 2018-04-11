def array_sum(lst,sum):
    seen=set()
    output=set()
    target=0

    for i in lst:
        target = sum-i
        if target not in seen:
            seen.add(i)
        else:
            output.add((max(target,i),min(target,i)))
    return output

print(array_sum([1,2,3,4,6],5))


