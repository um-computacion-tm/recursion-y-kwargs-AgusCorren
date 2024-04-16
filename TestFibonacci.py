import unittest

def fibonacci(n):
    if n in (0, 1):
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

class TestFibonacci(unittest.TestCase):
    def test_with_0(self):
        resultado = fibonacci(0)
        self.assertEqual(resultado, 0)

    def test_with_1(self):
        resultado = fibonacci(1)
        self.assertEqual(resultado, 1)

    def test_with_2(self):
        resultado = fibonacci(2)
        self.assertEqual(resultado, 1)

    def test_with_5(self):
        resultado = fibonacci(5)
        self.assertEqual(resultado, 5)
    
    def test_with_6(self):
        resultado = fibonacci(6)
        self.assertEqual(resultado, 8)

    def test_with_15(self):
        resultado = fibonacci(15)
        self.assertEqual(resultado, 610)

    def test_with_12(self):
        resultado = fibonacci(12)
        self.assertEqual(resultado, 144)

    def test_with_13(self):
        resultado = fibonacci(13)
        self.assertEqual(resultado, 233)

if __name__ == "__main__":
    unittest.main()