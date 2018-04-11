def get_fib(num):
    a,b=0,1
    for i in range(1,num+1):
        a,b=a+b,b
        print(a,end=" ")

get_fib(5)

print("\n")

def get_fib_rec(num):
    if num<=1:
        return 1
    else:
        return get_fib_rec(num-1)+get_fib_rec(num-2)


for i in range(1,5):
    print(get_fib_rec(i),end=" ")

