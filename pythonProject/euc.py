str1 = 'abc'
str2 = 'pqr'

# for s1 in str1:
#     for s2 in str2:
#         print(s1)
#         print(s2)

def fibonacci(n):
    if n < 0:
        raise ValueError("Number of terms must be non-negative")
        
    # Initialize first two numbers
    a, b = 0, 1
    # Create list to store series
    fib_series = []
    
    # Generate series up to n terms
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    
    return fib_series

# Example usage
n_terms = 10
result = fibonacci(n_terms)
print(f"Fibonacci series with {n_terms} terms:", result)

import unittest

class TestFibonacci(unittest.TestCase):
    def test_fibonacci_basic(self):
        """Test basic fibonacci sequence generation"""
        self.assertEqual(fibonacci(5), [0, 1, 1, 2, 3])
        
    def test_fibonacci_zero_terms(self):
        """Test with zero terms"""
        self.assertEqual(fibonacci(0), [])
        
    def test_fibonacci_one_term(self):
        """Test with one term"""
        self.assertEqual(fibonacci(1), [0])
        
    def test_fibonacci_two_terms(self):
        """Test with two terms"""
        self.assertEqual(fibonacci(2), [0, 1])
        
    def test_fibonacci_negative(self):
        """Test with negative input"""
        with self.assertRaises(ValueError):
            fibonacci(-1)

if __name__ == '__main__':
    unittest.main()


