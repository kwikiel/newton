from math import ceil
import unittest
'''
Eratostenes sieve
'''
def prime_test(n):
    if n==2 or n==3 or n==5:
        return True
    for i in range(2,int(n/2)):
        if n%i==0:
            return True
    return True

for i in range(1,1000):
    if prime_test(i):
        print i


class MathChecker(unittest.TestCase):

    def test_small_primes(self):
        self.assertTrue(prime_test(2))
        self.assertFalse(prime_test(4))

if __name__ == '__main__':
    unittest.main()
