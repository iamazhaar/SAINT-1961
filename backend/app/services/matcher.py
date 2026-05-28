from sympy import Symbol, Wild, sin, cos, tan, sec, csc, cot, asin, acos, atan, asec, acsc, acot, exp, log, sqrt

# Define the integration variable
x = Symbol('x')

# Define 'Wild' variables (placeholders for pattern matching)
c = Wild('c', exclude=[x, 0])
n = Wild('n', exclude=[x, -1]) 
m = Wild('m', exclude=[x, 0])

"""
SAINT's 26 Standard Forms (a-z) translated into SymPy.
Note: Slagle ignored the constant of integration (+ C), so we do too.
"""
STANDARD_FORMS = {
    # a. Constants
    c: c * x,
    
    # u. Polynomials (Slagle listed this as 'u')
    x**n: (x**(n + 1)) / (n + 1),
    
    # t. Inverse x
    x**-1: log(x),
    
    # b. Exponential base e
    exp(x): exp(x),
    
    # c. Exponential base c
    c**x: (c**x) / log(c),
    
    # d. Natural Logarithm
    log(x): x * log(x) - x,
    
    # e. Logarithm base c
    log(x, c): x * log(x, c) - x / log(c),
    
    # f. Sine
    sin(x): -cos(x),
    
    # g. Cosine
    cos(x): sin(x),
    
    # h. Tangent
    tan(x): log(sec(x)),
    
    # i. Cotangent
    cot(x): log(sin(x)),
    
    # j. Secant
    sec(x): log(sec(x) + tan(x)),
    
    # k. Cosecant
    csc(x): log(csc(x) - cot(x)),
    
    # l. Arcsine
    asin(x): x * asin(x) + sqrt(1 - x**2),
    
    # m. Arccosine
    acos(x): x * acos(x) - sqrt(1 - x**2),
    
    # n. Arctangent
    atan(x): x * atan(x) - (1/2) * log(1 + x**2),
    
    # o. Arccotangent
    acot(x): x * acot(x) + (1/2) * log(1 + x**2),
    
    # p. Arcsecant
    asec(x): x * asec(x) - log(x + sqrt(x**2 - 1)),
    
    # q. Arccosecant
    acsc(x): x * acsc(x) + log(x + sqrt(x**2 - 1)),
    
    # r. Secant squared
    sec(x)**2: tan(x),
    
    # s. Cosecant squared
    csc(x)**2: -cot(x),
    
    # v. Secant * Tangent
    sec(x) * tan(x): sec(x),
    
    # w. Cosecant * Cotangent
    csc(x) * cot(x): -csc(x),
    
    # x, y, z. Trigonometric Product Identities
    sin(m*x) * cos(n*x): -cos((m-n)*x) / (2*(m-n)) - cos((m+n)*x) / (2*(m+n)),
    sin(m*x) * sin(n*x):  sin((m-n)*x) / (2*(m-n)) - sin((m+n)*x) / (2*(m+n)),
    cos(m*x) * cos(n*x):  sin((m-n)*x) / (2*(m-n)) + sin((m+n)*x) / (2*(m+n)),
}

def match_standard_form(expr):
    """
    Checks if the parsed expression perfectly matches a standard form.
    Returns the integrated expression if matched, otherwise None.
    """
    for pattern, integrated_result in STANDARD_FORMS.items():
        match = expr.match(pattern)
        if match is not None:
            return integrated_result.subs(match)
    return None