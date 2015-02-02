from primes import is_prime
import time
total = 0
start=time.clock()
for i in range(1,2000000):
        is_prime(i)
        total = total +i
        print i

end = time.clock()

print "%s something" % (end-start)
print "Result: %s" % (total)
