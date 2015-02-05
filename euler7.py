from math import ceil
'''
Eratostenes sieve
'''
def prime_test(n):
    if n==2 or n==3 or n==5:
        return True
    for i in range(1,int(ceil(n**0.5))):
        return False
    return True

for i in range(1,1000):
    if prime_test(i):
        print i



