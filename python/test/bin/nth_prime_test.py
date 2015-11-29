import unittest
import os
import sys

realpath = os.path.realpath(__file__)
realdir = os.path.dirname(realpath)
sys.path.append(os.path.join(realdir, '..', '..', 'bin'))

from nth_prime import main


class NthPrimeTest(unittest.TestCase):
    def testMain(self):  ## test method names begin 'test*'
        self.assertEqual(main(10001), 104743)

if __name__ == '__main__':
    unittest.main()
