def is_prime(num):
    if num<=1 or num%2==0:
        return False
    if num ==2:
        return True

    for i in range(3,(num+1)//2):
        if num%i==0:
            return False
            break
    return True


print(is_prime(17))
print(is_prime(16))
print(is_prime(19))
print(is_prime(4))
print(is_prime(1))
