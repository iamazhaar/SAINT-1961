from sympy import Symbol, Add, Mul
from .matcher import match_standard_form

x = Symbol('x')

def integrate_linear_expression(expr):
    """
    Recursively applies the Sum Rule and Constant Multiple Rule.
    If it breaks the expression down to a standard form, it solves it.
    If it cannot solve a piece, it returns None.
    """
    # 1. Base Case: Try an immediate standard form match first
    standard_result = match_standard_form(expr)
    if standard_result is not None:
        return standard_result

    # 2. The Sum Rule: ∫ [f(x) + g(x)] dx = ∫ f(x) dx + ∫ g(x) dx
    if isinstance(expr, Add):
        integrated_parts = []
        for term in expr.args: # expr.args splits (x^2 + sin(x)) into [x^2, sin(x)]
            result = integrate_linear_expression(term)
            if result is None:
                return None # If any single part fails, the whole linear attempt fails
            integrated_parts.append(result)
        return Add(*integrated_parts) # Reconstruct the sum with the integrated parts

    # 3. The Constant Multiple Rule: ∫ c * f(x) dx = c * ∫ f(x) dx
    if isinstance(expr, Mul):
        # as_independent(x) splits the expression into (constant_part, x_dependent_part)
        # e.g., 5*x^2 becomes (5, x^2)
        constant_part, function_part = expr.as_independent(x)
        
        # If there actually is a constant to pull out (not just 1)
        if constant_part != 1:
            result = integrate_linear_expression(function_part)
            if result is not None:
                return constant_part * result

    # 4. If it's not a sum, not a constant multiple, and not a standard form...
    # We need the Step 4 Heuristic Goal Tree (Substitution, Parts, etc.)
    return None