def get_fact(num):
    fact = 1

    for i in range(1,num+1):
        fact = fact * i
    return fact

print(get_fact(5))


def get_fact_rec(num):
    if num==1:
        return num
    else:
        return num * get_fact_rec(num-1)

print(get_fact_rec(4))