from random import randint

def milrab(p):
    if p == 1: return False
    if p == 2: return True
    if p % 2 == 0: return False
    m, k = p - 1, 0
    while m % 2 == 0:
        m, k = m // 2, k + 1
    a = randint(2, p - 1)
    x = pow(a, m, p)
    if x == 1 or x == p - 1: return True
    while k > 1:
        x = pow(x, 2, p)
        if x == 1: return False
        if x == p - 1: return True
        k = k - 1
    return False

def is_prime(p, r = 40, c = 0):
    for i in range(r):
        if milrab(p) == True: c += 1
    if c == r: return True
    else: return False
