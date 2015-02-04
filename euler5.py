from math import factorial
def is_divisible_by_20(n):
    d=True
    for i in range(1,20):
        if n%i!=0:
            d=False
    return d


largest = factorial(20)
current = largest

for i in range(1,20):
    if current%i==0 and is_divisible_by_20(current/i):
        current=current/i
        print current

