import random


def otp(length):
    otp_ = ""
    for i in range(length):
        otp_ += str(random.randint(0, 9))
    return int(otp_)


# print(otp(6))


def fact(n):
    # print(n)
    if n > 1:
        # print(fact(n-1))
        return n * fact(n - 1)
    else:
        # print(fact(n - 1))
        assert n in (0, 1)
        return 1


a = fact(500)

n = 500
for i in range(n, 1, -1):
    s = i - 1
    n = n * s
