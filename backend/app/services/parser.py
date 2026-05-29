from sympy.parsing.sympy_parser import (
    parse_expr,
    standard_transformations,
    implicit_multiplication_application
)
import re



## Infix Expression -> SymPy Expression Tree ##
def parse_infix_expression(infix_expression: str):
    ## Fixing Frontend Formatting Issue: "pix" -> "pi*x" ##
    cleaned_infix_expr = re.sub(
        r'pi([a-zA-Z])',
        r'pi*\1',
        infix_expression
    )

    ## Convert '^' Into Python Power Operator '**' ##
    cleaned_infix_expr = cleaned_infix_expr.replace('^', '**')
    
    ## Implicit Multiplication Allowed -> So, Parse User Input Like 2x as 2*x ##
    transformations = (
        standard_transformations +
        (implicit_multiplication_application,)
    )

    try:
        ## Parsing The Infix Expression Into A Symbolic Expression Tree ##
        parsed_expression_tree = parse_expr(
            cleaned_infix_expr,
            transformations=transformations
        )
        
        return parsed_expression_tree
    
    except Exception as error:
        raise ValueError(
            f"Invalid mathematical expression: {str(error)}"
        )