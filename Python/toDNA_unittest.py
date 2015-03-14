## Basic unittest class

from toDNA import *
import random
import unittest

class TestMyFunctions(unittest.TestCase):
    
    # def setUp(self):
    #     self.seq = list(range(10))

    # def test_shuffle(self):
    #     # make sure the shuffled sequence does not lose any elements
    #     random.shuffle(self.seq)
    #     self.seq.sort()
    #     self.assertEqual(self.seq, list(range(10)))
    #     # should raise an exception for an immutable sequence
    #     self.assertRaises(TypeError, random.shuffle, (1,2,3))

    # def test_choice(self):
    #     element = random.choice(self.seq)
    #     self.assertTrue(element in self.seq)

    # def test_sample(self):
    #     with self.assertRaises(ValueError):
    #         random.sample(self.seq, 20)
    #     for element in random.sample(self.seq, 5):
    #         self.assertTrue(element in self.seq)
    
    def test_fib(self):
        self.assertTrue(fib(5))
        self.assertEqual(fib(1000),[0,1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987])

    def test_base10to4(self):
        self.assertTrue(base10to4(500))
        self.assertEqual(base10to4(500),'13310')

    def test_permutate(self):
        self.assertTrue(permutate("ACTG",2))
        self.assertEqual(permutate("ACTG",4),['ACTG','ACGT','ATCG','ATGC',
                                                            'AGCT','AGTC','CATG','CAGT',
                                                            'CTAG','CTGA','CGAT','CGTA',
                                                            'TACG','TAGC','TCAG','TCGA',
                                                            'TGAC','TGCA','GACT','GATC',
                                                            'GCAT','GCTA','GTAC','GTCA'])

    def test_pi_to_DNA(self):
        self.assertTrue(pi_to_DNA('pi.ale', 64, False))
        #self.assertEqual(pi_to_DNA('pi.ale', 64, False),missing)
        
    def test_fib_to_DNA(self):
        self.assertTrue(fib_to_DNA(5, 10, False))
        #self.assertEqual(fib_to_DNA(5, 10, False),missing)

if __name__ == '__main__':
    unittest.main()

