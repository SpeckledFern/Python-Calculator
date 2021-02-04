import unittest
import calculator


class TestCalculator(unittest.TestCase):
	def test_divide(self):
   		# Returns zero if attempting to divide by zero
		self.assertEqual(calculator.division(2, 0), 0)
	
		# Normal Division
		self.assertEqual(calculator.division(4, 2), 2)

		# Fractional division
		self.assertEqual(calculator.division(5, 2), 2.5)

	def test_add(self):
		# Normal Addition
		self.assertEqual(calculator.addition(2, 1), 3)

		# Negative Addition
		self.assertEqual(calculator.addition(5,-2), 3)
		
		# Float Addition 	
		self.assertEqual(calculator.addition(2.3, 1.2), 3.5)

	def test_sub(self):
		# Normal Subtraction
		self.assertEqual(calculator.subtract(2, 1), 1)

		# Negative Subtraction
		self.assertEqual(calculator.subtract(-2, -4), 2)
		
		# Float Subtraction
		self.assertEqual(calculator.subtract(8, 2.8), 5.2)

	def test_mult(self):
		# Normal multiplication	
		self.assertEqual(calculator.multiply(3, 4), 12)

		# Negative Multiplication
		self.assertEqual(calculator.multiply(3, -4), -12)

		# Float Multiply
		self.assertEqual(calculator.multiply(2, 1.5), 3)


if __name__ == "__main__":
	unittest.main()
