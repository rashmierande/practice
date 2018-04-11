def str_rev(inputStr):
    return "".join(inputStr[::-1])

print(str_rev("hello world"))


def sent_rev(inputSen):
    for word in inputSen[::-1]:
        print(word,end="")

sent_rev("hello world")
print("\n")

def sen_rev_inplace(inputStr):
    for word in inputStr.split():
        print(word[::-1],end=" ")

sen_rev_inplace("hello world")


