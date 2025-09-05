import numpy as np

"""
A solver to find intersection points (roots) between two mathematical functions.
"""
class FxSolver:
    NEAR_ZERO = 1e-9

    """
    This method finds the intersection points (roots) between two functions f1 and f2
    within the specified range [x_min, x_max] using a sampling and bisection method.
    Parameters:
    - f1: First function (callable)
    - f2: Second function (callable)
    - x_min: Minimum x value of the range (default: -10)
    - x_max: Maximum x value of the range (default: 10)
    - steps: Number of sampling steps (default: 5000)
    Returns:
    - List of tuples representing the intersection points (x, y)
    
    How it works:
    1. Define a new function g(x) = f1(x) - f2(x).
    2. Sample g(x) over the range [x_min, x_max] with the specified number of steps.
    3. Scan through the sampled values to detect sign changes, which indicate potential roots.
    4. For each detected sign change, use the bisection method to find the root more accurately.
    5. Return a list of (x, y) pairs where the functions intersect.
    6. If no intersections are found, an empty list is returned.
    """
    @staticmethod
    def find_roots(f1, f2, x_min=-10, x_max=10, steps=5000):
        # Define the difference function g(x) = f1(x) - f2(x)
        def g(x):
            return f1(x) - f2(x)

        # Sample g(x) over the specified range
        x_vals, g_vals = FxSolver._sample_function(g, x_min, x_max, steps)
        # Scan for roots in the sampled values
        roots = FxSolver._scan_for_roots(x_vals, g_vals, f1, g)
        return roots  # list of (x, y) pairs

    """
    This helper method samples the function g over a specified range [left, right]
    with a given number of steps.
    Parameters:
    - g: Function to sample (callable)
    - left: Left boundary of the range
    - right: Right boundary of the range
    - steps: Number of sampling steps
    Returns:
    - x_vals: Array of x values
    - g_vals: Array of corresponding g(x) values
    How it works:
    1. Generate an array of x values evenly spaced between left and right.
    2. Compute g(x) for each x value and store the results in g_vals
    3. Return both x_vals and g_vals as numpy arrays.
    """
    @staticmethod
    def _sample_function(g, left, right, steps):
        # Generate x values and compute g(x) for each x
        x_vals = np.linspace(left, right, steps)
        g_vals = np.array([g(x) for x in x_vals])
        return x_vals, g_vals

    """
    This helper method scans through the sampled g values to detect roots
    by looking for sign changes between consecutive samples.
    Parameters:
    - x_vals: Array of x values
    - g_vals: Array of corresponding g(x) values
    - f1: First function (callable)
    - g: Difference function g(x) = f1(x) - f2(x)
    Returns:
    - List of tuples representing the intersection points (x, y)
    How it works:
    1. Iterate through the g_vals array, checking pairs of consecutive values.
    2. If a sign change is detected (g1 * g2 < 0), it indicates a root exists between those x values.
    3. Use the bisection method to find the root more accurately.
    4. If an exact root is found (g1 or g2 is zero), add it directly to the results.
    5. Return a list of (x, y) pairs where the functions intersect.
    6. If no intersections are found, an empty list is returned.
    """
    @staticmethod
    def _scan_for_roots(x_vals, g_vals, f1, g):
        # Initialize list to hold found roots
        roots = []
        # Scan through g_vals to find sign changes
        for i in range(len(x_vals) - 1):
            # Get consecutive g values
            g1, g2 = g_vals[i], g_vals[i + 1]
            # If either value is NaN, skip this interval
            if np.isnan(g1) or np.isnan(g2):
                continue
            # If g1 or g2 is exactly zero, we found an exact root
            if g1 == 0.0:  # exact root
                roots.append((x_vals[i], f1(x_vals[i])))
            elif g2 == 0.0:  # exact root
                roots.append((x_vals[i + 1], f1(x_vals[i + 1])))
            # if there is a sign change, there is a root in between
            elif g1 * g2 < 0.0:
                # Use bisection method to find the root more accurately
                root = FxSolver._bisection(x_vals[i], x_vals[i + 1], g1, f1, g)
                roots.append(root)
        return roots

    """
    This helper method uses the bisection method to find a root of the function g
    within the interval [l, r] where g(l) and g(r) have opposite signs.
    This function uses a divide-and-conquer approach to iteratively narrow down the interval
    until it converges to a root or the interval is very small.
    Parameters:
    - l: Left boundary of the interval
    - r: Right boundary of the interval
    - g1: Value of g at the left boundary (g(l))
    - f1: First function (callable)
    - g: Difference function g(x) = f1(x) - f2(x)
    Returns:
    - Tuple representing the intersection point (x, y)
    How it works:
    1. Iteratively narrow down the interval [l, r] by checking the sign of g at the midpoint.
    2. If g(mid) is zero or the interval is very small, return the midpoint as the root.
    3. If g(l) and g(mid) have opposite signs, the root lies in [l, mid], so update r to mid.
    4. Otherwise, the root lies in [mid, r], so update l to mid.
    5. Repeat the process for a maximum of 100 iterations or until convergence.
    6. Return the midpoint and the corresponding f1 value as the intersection point.
    """
    @staticmethod
    def _bisection(l, r, g1, f1, g):
        # Loop 100 times to narrow down the interval or until convergence
        for _ in range(100):
            # Calculate midpoint
            mid = (l + r) / 2
            # Evaluate g at midpoint
            g_mid = g(mid)
            # If g(mid) is NaN, break out of the loop
            if np.isnan(g_mid):
                break
            # If g(mid) is zero or the interval is very small, return the midpoint as root
            if g_mid == 0.0 or abs(r - l) < FxSolver.NEAR_ZERO:
                return mid, f1(mid)
            # If g(l) and g(mid) have opposite signs, root is in [l, mid]
            if g1 * g_mid < 0.0:
                r = mid
            # Else root is in [mid, r]
            else:
                l = mid
        # Return midpoint and corresponding f1 value as the intersection point
        return (l + r) / 2, f1((l + r) / 2)
