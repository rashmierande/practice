def get_word_length(sen):
    for i in sen.split():
        print(i ,"-->",len(i))

get_word_length("hello darling how are you ?")

def get_length(sen):
    cnt={}
    for i in sen.split():
        cnt[i]=len(i)

    return cnt

print(get_length("hello darling how are you ?"))