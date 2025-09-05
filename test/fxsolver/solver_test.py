import unittest

from src.fxsolver.solver import FxSolver
from src.fxsolver.parser import ExpressionParser


class FxSolverTest(unittest.TestCase):
    def test_solve_linear(self):
        f1 = ExpressionParser.convert_expr_to_function("2*x + 3")
        f2 = ExpressionParser.convert_expr_to_function("5*x - 3")
        roots = FxSolver.find_roots(f1, f2)
        self.assertAlmostEqual(roots[0][0], 2)
        self.assertAlmostEqual(roots[0][1], f1(roots[0][0]))
        self.assertAlmostEqual(roots[0][1], f2(roots[0][0]))
        self.assertEqual(len(roots), 1)

    def test_solve_quadratic_vs_linear(self):
        f1 = ExpressionParser.convert_expr_to_function("x^2 - 4")
        f2 = ExpressionParser.convert_expr_to_function("3*x - 6")
        roots = FxSolver.find_roots(f1, f2)
        self.assertAlmostEqual(roots[0][0], 1)
        self.assertAlmostEqual(roots[0][1], f1(roots[0][0]))
        self.assertAlmostEqual(roots[0][1], f2(roots[0][0]))
        self.assertAlmostEqual(roots[1][0], 2)
        self.assertAlmostEqual(roots[1][1], f1(roots[1][0]))
        self.assertAlmostEqual(roots[1][1], f2(roots[1][0]))
        self.assertEqual(len(roots), 2)

    def test_no_roots(self):
        f1 = ExpressionParser.convert_expr_to_function("x^2 + 1")
        f2 = ExpressionParser.convert_expr_to_function("0")
        roots = FxSolver.find_roots(f1, f2)
        self.assertEqual(len(roots), 0)



if __name__ == '__main__':
    unittest.main()
