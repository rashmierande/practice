def is_uniqueChar(inputStr):
    inputStr=inputStr.lower()
    chars=set()

    for letter in inputStr:
        if letter not in chars:
            chars.add(letter)
        else:
            return False

    return True

print(is_uniqueChar("abbcADg"))
print(is_uniqueChar("abc"))

def is_unq(InputStr):
    return len(set(InputStr))==len(InputStr)

print(is_unq("abc"))
print(is_unq("abcda"))