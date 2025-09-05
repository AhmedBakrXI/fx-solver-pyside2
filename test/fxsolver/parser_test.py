import unittest

from src.fxsolver.parser import ExpressionParser

class ExpressionParserEvaluateTest(unittest.TestCase):
    def test_constant_func(self):
        f = ExpressionParser.convert_expr_to_function("5")
        self.assertEqual(f(10), 5)
        self.assertEqual(f(-3), 5)
        self.assertEqual(f(0), 5)

    def test_linear_func(self):
        f = ExpressionParser.convert_expr_to_function("2*x + 3")
        self.assertEqual(f(0), 3)
        self.assertEqual(f(1), 5)
        self.assertEqual(f(-1), 1)

    def test_quadratic_func(self):
        f = ExpressionParser.convert_expr_to_function("x^2 - 4*x + 4")
        self.assertEqual(f(0), 4)
        self.assertEqual(f(2), 0)
        self.assertEqual(f(4), 4)

    def test_sqrt_func(self):
        f = ExpressionParser.convert_expr_to_function("sqrt(x)")
        self.assertEqual(f(4), 2)
        self.assertEqual(f(0), 0)
        self.assertTrue(f(-1) != f(-1))

    def test_log10_func(self):
        f = ExpressionParser.convert_expr_to_function("log10(x)")
        self.assertEqual(f(10), 1)
        self.assertEqual(f(100), 2)
        self.assertTrue(f(0) != f(0))
        self.assertTrue(f(-10) != f(-10))

    def test_division_by_zero(self):
        f = ExpressionParser.convert_expr_to_function("1/x")
        self.assertEqual(f(1), 1)
        self.assertTrue(f(0) != f(0))
        self.assertEqual(f(-1), -1)

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            ExpressionParser.convert_expr_to_function("2*y + 3")
        with self.assertRaises(ValueError):
            ExpressionParser.convert_expr_to_function("2*x + unknown_func(3)")
        with self.assertRaises(ValueError):
            ExpressionParser.convert_expr_to_function("2**")
        with self.assertRaises(ValueError):
            ExpressionParser.convert_expr_to_function("4+")

    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            ExpressionParser.convert_expr_to_function("")
        with self.assertRaises(ValueError):
            ExpressionParser.convert_expr_to_function(None)

    def test_log10_and_sqrt_combined(self):
        f = ExpressionParser.convert_expr_to_function("log10(sqrt(x))")
        self.assertEqual(f(100), 1)
        self.assertEqual(f(10000), 2)
        self.assertTrue(f(0) != f(0))
        self.assertTrue(f(-10) != f(-10))


class ExpressionParserValidateTest(unittest.TestCase):
    def test_valid_expression(self):
        try:
            ExpressionParser.validate_expression("3*x^2 + 2*x + 1")
        except ValueError:
            self.fail("validate_expression raised ValueError unexpectedly!")

    def test_invalid_expression(self):
        with self.assertRaises(ValueError):
            ExpressionParser.validate_expression("3*x^2 + 2*y + 1")

    def test_empty_expression(self):
        with self.assertRaises(ValueError):
            ExpressionParser.validate_expression("")
        with self.assertRaises(ValueError):
            ExpressionParser.validate_expression("   ")

    def test_none_expression(self):
        with self.assertRaises(ValueError):
            ExpressionParser.validate_expression(None)


if __name__ == '__main__':
    unittest.main()
