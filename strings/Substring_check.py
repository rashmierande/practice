def isSubstr(str1,substr):
    if substr in str1:
        return True
    else:
        return False

print(isSubstr("hello world","world"))


def isSubstr1(str1,substr):
    len_word=len(substr)

    for word in range(len(str1)-1):
        # print(str1[word:word+len_word])
        if str1[word:word+len_word]==substr:
            return True
    return False

print(isSubstr1("hello world","world"))


import re
str1="hello world"
sub="world"
s= re.search(sub,str1)
print(s.group())
