sumakwadratow = 0
for i in range(1,101):
    print i
    sumakwadratow = sumakwadratow + i*i

print "Suma kwadratow: %s" % sumakwadratow

sks = 0
for i in range(1,101):
    sks = sks+i

print "Suma kwadratow sumy: %s" % (sks*sks)

print "Roznica: %s" % ((sks*sks)-sumakwadratow)
