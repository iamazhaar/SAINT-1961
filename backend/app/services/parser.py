from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
from sympy import Symbol, Integer, Float
import re

def string_to_saint_tree(expression_str: str):
    """
    Takes a raw infix string from the frontend, parses it safely, 
    and converts it into a nested dictionary/tuple representation 
    mirroring the LISP structural style used in Slagle's SAINT thesis.
    """
    # 1. Clean common frontend formatting quirks
    # If 'pi' is directly followed by a letter, inject a multiplier (e.g., pix -> pi*x)
    cleaned_str = re.sub(r'pi([a-zA-Z])', r'pi*\1', expression_str)
    cleaned_str = cleaned_str.replace('^', '**')
    
    # 2. Allow users to type '2x' instead of forcing '2*x' (Implicit Multiplication)
    transformations = standard_transformations + (implicit_multiplication_application,)
    
    try:
        # Parse into a SymPy expression object safely
        sympy_expr = parse_expr(cleaned_str, transformations=transformations)
        return sympy_expr
    except Exception as e:
        raise ValueError(f"Syntactically invalid mathematical input: {str(e)}")

def inspect_structure(expr):
    """
    A helper function to show you how Python sees the structural 
    parts of the math expression tree.
    """
    if expr.is_Atom:
        return str(expr)
    
    # Returns (OPERATOR, [OPERANDS/ARGUMENTS])
    return (expr.__class__.__name__, [inspect_structure(arg) for arg in expr.args])