def collatz(n):
    counter = 0
    while(n>=4):

        print n
        counter = counter+1
        if n%2==0:
            n=n/2
        else:
            n=3*n+1
        return counter


