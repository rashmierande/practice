def sumNum(num):
    sum=0
    if num==0:
        return 0
    for i in str(num):
        sum=sum+int(i)
    return sum


print(sumNum(1230))