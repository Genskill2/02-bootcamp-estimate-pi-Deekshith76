import math
import unittest
from random import *

class TestWallis(unittest.TestCase):
    def test_low_iters(self):
        for i in range(0, 5):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) > 0.15, msg=f"Estimate with just {i} iterations is {pi} which is too accurate.\n")
            
    def test_high_iters(self):
        for i in range(500, 600):
            pi = wallis(i)
            self.assertTrue(abs(pi - math.pi) < 0.01, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")


class TestMC(unittest.TestCase):
    def test_randomness(self):
        pi0 = monte_carlo(15000)
        pi1 = monte_carlo(15000)
        
        self.assertNotEqual(pi0, pi1, "Two different estimates for PI are exactly the same. This is almost impossible.")

        self.assertFalse(abs(pi0 - pi1) > 0.05, "Two different estimates of PI are too different. This should not happen")

    def test_accuracy(self):
        for i in range(500, 600):
            pi = monte_carlo(i)
            self.assertTrue(abs(pi - math.pi) < 0.4, msg=f"Estimate with even {i} iterations is {pi} which is not accurate enough.\n")
        
def wallis(n):
    product = 1
    for i  in range(1,n+1):
        val = (4*(i**2))/((4*(i**2))-1)
        product *= val
    pi_val = 2*product
    return pi_val
 

def monte_carlo(n):
    circle_points = 0
    square_points = 0
    for i in range(n):
        p = random()
        q = random()
        if (p**2 + q**2 <=1):
            circle_points += 1
        square_points += 1
    ratio = circle_points/square_points
    pi_val = 4*ratio
    return pi_val
        
if __name__ == "__main__":
    unittest.main()
