a=1
b=2
suma=0
while(b<4000000 and a<4000000):
    if(a%2==0 and a<4000000):
        suma=suma+a
        print a
    if(b%2==0 and b<4000000):
        suma=suma+b
        print b
    a=a+b
    b=a+b
print "suma: "
print suma
