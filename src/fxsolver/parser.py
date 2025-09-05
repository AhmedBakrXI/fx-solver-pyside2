import math
import re
import numpy as np

"""
A simple parser to convert mathematical expressions in string format into callable functions.
Supports basic arithmetic operations, exponentiation, and functions like sqrt and log10.
"""
class ExpressionParser:
    # Regex to identify any characters not allowed in the expression after removing valid parts
    regexNotAllowed = r"[A-Za-z_]+"

    # Allowed functions that can be used in the expressions
    ALLOWED_FUNCTIONS = {
        "sqrt": math.sqrt,
        "log10": math.log10,
    }

    """
    Converts a mathematical expression in string format to a callable function of x.
    """
    @staticmethod
    def convert_expr_to_function(expression: str):
        # Basic validation
        if not expression or not isinstance(expression, str):
            raise ValueError("Expression must be a non-empty string.")

        # Replace '^' with '**' for exponentiation
        expression = expression.strip().replace("^", "**")
        # Check for invalid characters in the expression
        ExpressionParser.validate_expression(expression)

        # Define the function that evaluates the expression
        def f(x):
            # Create a local dictionary of allowed functions and the variable x
            local_subs = {"x": x, **ExpressionParser.ALLOWED_FUNCTIONS}
            try:
                # Safely evaluate the expression using eval with restricted built-ins
                return eval(expression, {"__builtins__": {}}, local_subs)
            except (ZeroDivisionError, SyntaxError, ValueError):
                return np.nan
            except Exception as e:
                raise ValueError(f"Error evaluating expression: {e}")

        return f

    @staticmethod
    def validate_expression(expression: str):
        expr_test = expression.replace("x", "").replace("log10", "").replace("sqrt", "")
        is_bad = re.search(ExpressionParser.regexNotAllowed, expr_test)
        # If any invalid characters are found, raise an error
        if is_bad:
            raise ValueError(f"Expression contains invalid characters: {is_bad.group(0)}")
