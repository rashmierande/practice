def get_power(num,pow):

    if pow == 0:
        return 1
    else:
        return num*get_power(num,pow-1)

print(pow(2,3))


