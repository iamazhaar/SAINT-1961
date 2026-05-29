from sympy import Symbol, Add, Mul
from .matcher import match_standard_form


x = Symbol('x')


## RECURSIVELY APPLY LINEARITY & CHECK FOR STANDARD FORM ##
def integrate_linear_expression(parsed_expression_tree):
    ## BASE CASE: TRY AN IMMEDIATE STANDARD FORM MATCH FIRST ##
    standard_result = match_standard_form(parsed_expression_tree)
    if standard_result is not None:
        return standard_result

    ## RECURSIVE CASE: THE SUM RULE ##
    if isinstance(parsed_expression_tree, Add):
        integrated_parts = []
        ## expr.args SPLITS (x^2 + sin(x)) INTO (x^2, sin(x)) ##
        for term in parsed_expression_tree.args:
            result = integrate_linear_expression(term)
            if result is None:
                return None
            integrated_parts.append(result)
        return Add(*integrated_parts)

    ## RECURSIVE CASE: THE PRODUCT RULE ##
    if isinstance(parsed_expression_tree, Mul):
        ## as_independent(x) SPLITS THE EXPRESSION INTO (constant_part, x_dependent_part) ##
        ## e.g., 5*x^2 becomes (5, x^2) ##
        constant_part, function_part = parsed_expression_tree.as_independent(x)
        
        ## IF THERE ACTUALLY IS A CONSTANT TO PULL OUT (NOT JUST 1) ##
        if constant_part != 1:
            result = integrate_linear_expression(function_part)
            if result is not None:
                return constant_part * result

    return None