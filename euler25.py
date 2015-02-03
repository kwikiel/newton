a=1
b=1
suma=0
term = 0
while(len(str(a))<=1000):
    term = term + 2
    print "Term: %s Equals: %s and has %s digits" % (term-1, a, len(str(a)))
    print "Term: %s Equals: %s and has %s digits" % (term, b, len(str(a)))
    a=a+b
    b=a+b
