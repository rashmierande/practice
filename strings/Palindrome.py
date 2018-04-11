def is_Palin(str1):
    return str1[::-1]== str1

print(is_Palin("hello"))
print(is_Palin("123"))
print(is_Palin("111"))
print(is_Palin("aba"))

def is_pal(str1):
    r=str1[::-1]
    for i in range(0,len(str1)+1//2):
        if str1[i]!=r[i]:
            return False
    return True

print(is_pal("aabac17"))