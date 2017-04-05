# TestBMICalculator.py

# What are we testing for?

# Wide range of inputs
    # - proper and improper
# Boundary Conditions
# Correct outputs
# Test for exceptions

# Import Statements
import unittest
import BMICalculator

class KnownValues(unittest.TestCase):
    # Formula for unittest method is:
    # test_functionName_testDescription

    def test_calculateBMI_forNormalBoundary(self):
        # Capture the results of the function
        result = BMICalculator.calculateBMI(62, 120)
        # Check for expected output
        self.assertEqual(22, result)

    def test_calculateBMI_forFirstNormalValueLowerHeight(self):
        result = BMICalculator.calculateBMI(60, 123)
        expected = 24
        self.assertEqual(expected, result)

    # Add minimum of 5 more unittests
    def test_calculateBMI_forTallNormalValueLowerHeight(self):
        result = BMICalculator.calculateBMI(76, 197)
        expected = 24
        self.assertEqual(expected, result)

    def test_calculateBMI_for1stOverweightValue(self):
        result = BMICalculator.calculateBMI(64, 157)
        expected = 27
        self.assertEqual(expected, result)

    def test_calculateBMI_for2ndOverweightValue(self):
        result = BMICalculator.calculateBMI(59, 143)
        expected = 29
        self.assertEqual(expected, result)

    def test_calculateBMI_for1stObeseValue(self):
        result = BMICalculator.calculateBMI(67, 204)
        expected = 32
        self.assertEqual(expected, result)

    def test_calculateBMI_for2ndObeseValue(self):
        result = BMICalculator.calculateBMI(69, 230)
        expected = 34
        self.assertEqual(expected, result)

    def test_calculateBMI_for3rdObeseValue(self):
        result = BMICalculator.calculateBMI(61, 185)
        expected = 35
        self.assertEqual(expected, result)

    def test_calculateBMI_for4thObeseValue(self):
        result = BMICalculator.calculateBMI(69, 250)
        expected = 37
        self.assertEqual(expected, result)

    def test_calculateBMI_for5thObeseValue(self):
        result = BMICalculator.calculateBMI(75, 287)
        expected = 36
        self.assertEqual(expected, result)

    def test_calculateBMI_for6thObeseValue(self):
        result = BMICalculator.calculateBMI(70, 271)
        expected = 39
        self.assertEqual(expected, result)

    def test_calculateBMI_forLowNormalValue(self):
        result = BMICalculator.calculateBMI(58, 91)
        expected = 19
        self.assertEqual(expected, result)

    def test_calculateBMI_for2ndExtremeObeseValue(self):
        result = BMICalculator.calculateBMI(66, 260)
        expected = 42
        self.assertEqual(expected, result)

    def test_calculateBMI_for3rdExtremeObeseValue(self):
        result = BMICalculator.calculateBMI(58, 258)
        expected = 54
        self.assertEqual(expected, result)

    def test_calculateBMI_for4thExtremeObeseValue(self):
        result = BMICalculator.calculateBMI(74, 420)
        expected = 54
        self.assertEqual(expected, result)

    def test_calculateBMI_for5thExtremeObeseValue(self):
        result = BMICalculator.calculateBMI(76, 443)
        expected = 54
        self.assertEqual(expected, result)



# Run the tests
if __name__ == '__main__':
    unittest.main()
