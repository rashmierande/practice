def get_word_freq(filename):
    cnt={}

    with open(filename,"r") as f:
        lst=f.read().split()


    for word in lst:
        if word in cnt:
            cnt[word]+=1
        else:
            cnt[word]=1

    return cnt


print(get_word_freq("word_cnt.txt"))


def get_word_freq1(filename,findword):
    cnt={}
    with open(filename,"r") as f:
        lst=f.read().split()

    for word in lst:
        if word==findword:
            if word in cnt:
                cnt[word]+=1
            else:
                cnt[word]=1
    return cnt

print(get_word_freq1("word_cnt.txt","People"))
