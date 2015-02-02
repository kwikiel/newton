from math import ceil

def is_prime(n):
    if n==1:
        return False
    if n==2:
        return True
    if n==3:
        return True
    if n==4:
        return False
    else:
        for i in range(2,int(ceil(n**0.5))):
            if n%i==0:
                return False
        return True



