def anagram(str1,str2):
    str1=str1.replace(' ',"").lower()
    str2=str2.replace(' ',"").lower()

    cnt={}

    if len(str1)!=len(str2):
        return False

    if len(str1)==1:
        return True

    for letter in str1:
        if letter in cnt:
            cnt[letter]+=1
        else:
            cnt[letter]=1

    for letter in str2:
        if letter in cnt:
            cnt[letter]-=1
        else:
            cnt[letter]=1

    for i in cnt:
        if cnt[i]!=0:
            return False
    return True

print(anagram("abc1","cba1"))
