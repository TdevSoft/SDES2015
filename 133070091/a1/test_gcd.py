import gcd
import unittest

class TestGCD(unittest.TestCase):
      def test_gcd(self):
         self.assertEqual(gcd.gcd(40,12), 4)
         self.assertEqual(gcd.gcd(400,120), 40)
         self.assertEqual(gcd.gcd(0,120), 120)

      def test_valueError(self):
         self.assertRaises(ValueError, gcd.gcd, 40, -12)
         self.assertRaises(ValueError, gcd.gcd, -40, 12)
         self.assertRaises(ValueError, gcd.gcd, -40, -12)
      def test_TypeError(self):
         self.assertRaises(TypeError, gcd.gcd, '40', -12)
         self.assertRaises(TypeError, gcd.gcd, -40, 12.0)
         self.assertRaises(TypeError, gcd.gcd, -40, -12.2)

if __name__ == '__main__':
         unittest.main()


