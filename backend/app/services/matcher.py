from sympy import Symbol, Wild, sin, cos, tan, sec, csc, cot, asin, acos, atan, asec, acsc, acot, exp, log, sqrt


x = Symbol('x')
c = Wild('c', exclude=[x, 0])
n = Wild('n', exclude=[x, -1])
m = Wild('m', exclude=[x, 0])


## SAINT'S 26 STANDARD FORMS TRANSLATED INTO SYMPY ##
STANDARD_FORMS = {
    c: c * x,
    x**n: (x**(n + 1)) / (n + 1),
    x**-1: log(x),

    exp(x): exp(x),
    c**x: (c**x) / log(c),

    log(x): x * log(x) - x,
    log(x, c): x * log(x, c) - x / log(c),

    sin(x): -cos(x),
    cos(x): sin(x),
    tan(x): log(sec(x)),
    cot(x): log(sin(x)),
    sec(x): log(sec(x) + tan(x)),
    csc(x): log(csc(x) - cot(x)),

    asin(x): x * asin(x) + sqrt(1 - x**2),
    acos(x): x * acos(x) - sqrt(1 - x**2),
    atan(x): x * atan(x) - (1/2) * log(1 + x**2),
    acot(x): x * acot(x) + (1/2) * log(1 + x**2),
    asec(x): x * asec(x) - log(x + sqrt(x**2 - 1)),
    acsc(x): x * acsc(x) + log(x + sqrt(x**2 - 1)),
    
    sec(x)**2: tan(x),
    csc(x)**2: -cot(x),
    sec(x) * tan(x): sec(x),
    csc(x) * cot(x): -csc(x),
    
    sin(m*x) * cos(n*x): -cos((m-n)*x) / (2*(m-n)) - cos((m+n)*x) / (2*(m+n)),
    sin(m*x) * sin(n*x):  sin((m-n)*x) / (2*(m-n)) - sin((m+n)*x) / (2*(m+n)),
    cos(m*x) * cos(n*x):  sin((m-n)*x) / (2*(m-n)) + sin((m+n)*x) / (2*(m+n)),
}


def match_standard_form(expr):
    for pattern, integrated_result in STANDARD_FORMS.items():
        match = expr.match(pattern)
        if match is not None:
            return integrated_result.subs(match)
        
    return None