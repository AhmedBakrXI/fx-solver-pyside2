import numpy as np

class FxSolver:
    NEAR_ZERO = 1e-6

    @staticmethod
    def find_root(f1, f2, x_min=-10, x_max=10, steps=5000, max_iters=5):
        def g(x):
            return f1(x) - f2(x)

        left, right = x_min, x_max
        for _ in range(max_iters):
            x_vals, g_vals = FxSolver._sample_function(g, left, right, steps)
            root = FxSolver._scan_for_root(x_vals, g_vals, f1, g)
            if root is not None:
                return root
            left, right = FxSolver._expand_search_range(left, right)
        return None, None

    @staticmethod
    def _sample_function(g, left, right, steps):
        x_vals = np.linspace(left, right, steps)
        g_vals = np.array([g(x) for x in x_vals])
        return x_vals, g_vals

    @staticmethod
    def _scan_for_root(x_vals, g_vals, f1, g):
        for i in range(len(x_vals) - 1):
            g1, g2 = g_vals[i], g_vals[i + 1]
            if np.isnan(g1) or np.isnan(g2):
                continue
            if g1 == 0.0:
                return x_vals[i], f1(x_vals[i])
            if g2 == 0.0:
                return x_vals[i + 1], f1(x_vals[i + 1])
            if g1 * g2 < 0.0:
                return FxSolver._bisection(x_vals[i], x_vals[i + 1], g1, f1, g)
        return None

    @staticmethod
    def _bisection(l, r, g1, f1, g):
        for _ in range(100):
            mid = (l + r) / 2
            g_mid = g(mid)
            if np.isnan(g_mid):
                break
            if g_mid == 0.0 or abs(r - l) < FxSolver.NEAR_ZERO:
                return mid, f1(mid)
            if g1 * g_mid < 0.0:
                r = mid
            else:
                l = mid
        return (l + r) / 2, f1((l + r) / 2)

    @staticmethod
    def _expand_search_range(left, right):
        width = left - right
        return left - width, right + width
