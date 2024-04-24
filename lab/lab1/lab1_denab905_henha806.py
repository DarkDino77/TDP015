# TDP015 Programming Assignment 1
# Logic
# Skeleton Code

import itertools


class Exp(object):
    """A Boolean expression.

    A Boolean expression is represented in terms of a *reserved symbol* (a
    string) and a list of *subexpressions* (instances of the class `Exp`).
    The reserved symbol is a unique name for the specific type of
    expression that an instance of the class represents. For example, the
    constant `True` uses the reserved symbol `1`, and logical and uses `∧`
    (the Unicode symbol for conjunction). The reserved symbol for a
    variable is its name, such as `x` or `y`.

    Attributes:
        sym: The reserved symbol of the expression (a string).
        sexps: The list of subexpressions (instances of the class `Exp`).
    """

    def __init__(self, sym, *sexps):
        """Constructs a new expression.

        Args:
            sym: The reserved symbol for this expression.
            sexps: The list of subexpressions.
        """
        self.sym = sym
        self.sexps = sexps

    def value(self, assignment):
        """Returns the value of this expression under the specified truth
        assignment.

        Args:
            assignment: A truth assignment, represented as a dictionary
            that maps variable names to truth values.

        Returns:
            The value of this expression under the specified truth
            assignment: either `True` or `False`.
        """
        raise ValueError()

    def variables(self):
        """Returns the (names of the) variables in this expression.

        Returns:
           The names of the variables in this expression, as a set.
        """
        variables = set()
        for sexp in self.sexps:
            variables |= sexp.variables()
        return variables


class Var(Exp):
    """A variable."""

    def __init__(self, sym):
        super().__init__(sym)

    def value(self, assignment):
        assert len(self.sexps) == 0
        return assignment[self.sym]

    def variables(self):
        assert len(self.sexps) == 0
        return {self.sym}


class Nega(Exp):
    """Logical not."""

    def __init__(self, sexp1):
        super().__init__('¬', sexp1)

    def value(self, assignment):
            assert len(self.sexps) == 1
            return not self.sexps[0].value(assignment)


class Conj(Exp):
    """Logical and."""

    def __init__(self, sexp1, sexp2):
        super().__init__('∧', sexp1, sexp2)

    def value(self, assignment):
        assert len(self.sexps) == 2
        return \
            self.sexps[0].value(assignment) and \
            self.sexps[1].value(assignment)


class Disj(Exp):
    """Logical or."""

    def __init__(self, sexp1, sexp2):
        super().__init__('∨', sexp1, sexp2)

    def value(self, assignment):
        assert len(self.sexps) == 2
        return \
            self.sexps[0].value(assignment) or \
            self.sexps[1].value(assignment)


class Impl(Exp):
    """Logical implication."""

    def __init__(self, sexp1, sexp2):
        super().__init__('→', sexp1, sexp2)

    def value(self, assignment):
        assert len(self.sexps) == 2

        if not self.sexps[0].value(assignment) or self.sexps[1].value(assignment):
            return True
        else:
            return False



class Equi(Exp):
    """Logical equivalence."""

    def __init__(self, sexp1, sexp2):
        super().__init__('↔', sexp1, sexp2)

    def value(self, assignment):
        assert len(self.sexps) == 2

        return  self.sexps[0].value(assignment) == self.sexps[1].value(assignment)



def assignments(variables):
    """Yields all truth assignments to the specified variables.

    Args:
        variables: A set of variable names.

    Yields:
        All truth assignments to the specified variables. A truth
        assignment is represented as a dictionary mapping variable names to
        truth values. Example:

        {'x': True, 'y': False}
    """

    for values in itertools.product([True,False], repeat=len(variables)):
        #print(dict(zip(variables,values)))
        yield dict(zip(variables,values))
    


def satisfiable(exp):
    """Tests whether the specified expression is satisfiable.

    An expression is satisfiable if there is a truth assignment to its
    variables that makes the expression evaluate to true.

    Args:
        exp: A Boolean expression.

    Returns:
        A truth assignment that makes the specified expression evaluate to
        true, or False in case there does not exist such an assignment.
        A truth assignment is represented as a dictionary mapping variable
        names to truth values.
    """

    for assignment in assignments(exp.variables() ):
        if exp.value(assignment):
            return assignment
    return False

def tautology(exp):
    """Tests whether the specified expression is a tautology.

    An expression is a tautology if it evaluates to true under all
    truth assignments to its variables.

    Args:
        exp: A Boolean expression.

    Returns:
        True if the specified expression is a tautology, False otherwise.
    """

    return all(exp.value(assignment)for assignment in assignments(exp.variables()))


def equivalent(exp1, exp2):
    """Tests whether the specified expressions are equivalent.

    Two expressions are equivalent if they have the same truth value under
    each truth assignment.

    Args:
        exp1: A Boolean expression.
        exp2: A Boolean expression.

    Returns:
        True if the specified expressions are equivalent, False otherwise.
    """
    return all(exp1.value(assignment) == exp2.value(assignment) for assignment in assignments(exp1.variables() | exp2.variables()))


def test1():
    a = Var('a')
    b = Var('b')
    c = Var('c')
    exp1 = Impl(Impl(a, b), c)
    exp2 = Conj(Disj(a, c), Disj(Nega(b), c))
    return equivalent(exp1, exp2)

def test2():
    a = Var('a')
    exp = Disj(a, Nega(a))
    return tautology(exp)

def test3():
    p = Var('p')
    q = Var('q')
    exp = Equi(Nega(Conj(p, q)), Disj(Nega(p), Nega(q)))
    return tautology(exp)

def test4():
    p = Var('p')
    q = Var('q')
    r = Var('r')
    exp = Impl(Conj(Impl(q,r),Conj(Impl(p,r),Conj(p,q))),r)
    return tautology(exp)

def test5():
    a = Var('a')
    b = Var('b')
    exp = Conj(a, b)
    return tautology(exp)

    
def test6():
    x = Var('x')
    exp = Nega(Nega(x))
    return equivalent(exp, x)

def test7():
    p = Var('p')
    q = Var('q')
    exp = Impl(p, q)
    not_p_or_q = Disj(Nega(p), q)
    return equivalent(exp, not_p_or_q)

def test8():
    x = Var('x')
    y = Var('y')
    exp = Disj(Conj(x, y), Conj(Nega(x), Nega(y)))
    return satisfiable(exp)

def test9():
    a = Var('a')
    exp = Nega(Nega(a))
    return equivalent(a, exp)

def test10():
    p = Var('p')
    not_p = Nega(p)
    exp = Conj(p, not_p)
    return satisfiable(exp)

def test11():
    x = Var('x')
    exp = Nega(Nega(Nega(Nega(x))))
    return equivalent(exp, x)

def test12():
    p = Var('p')
    q = Var('q')
    r = Var('r')
    exp = Impl(Impl(p, q), r)
    not_p_or_q_or_r = Disj(Disj(Nega(p), q), r)
    return equivalent(exp, not_p_or_q_or_r)

def test13():
    x = Var('x')
    y = Var('y')
    z = Var('z')
    exp = Disj(Conj(x, Disj(Nega(y), z)), Conj(Nega(x), Nega(y)))
    return satisfiable(exp)

def test14():
    a = Var('a')
    b = Var('b')
    exp = Nega(Nega(Conj(a, Nega(b))))
    return equivalent(exp, Conj(a, Nega(b)))

def test15():
    p = Var('p')
    q = Var('q')
    exp = Conj(Conj(p, Nega(p)), Conj(q, Nega(q)))
    return satisfiable(exp) 

if __name__ == "__main__":
    print("Test 1 (Should be true):", test1())
    print("Test 2 (Should be true):", test2())
    print("Test 3 (Should be true):", test3())
    print("Test 4 (Should be true):", test4())
    print("Test 5 (Should be false):", test5())
    print("Test 6 (Should be true):", test6())
    print("Test 7 (Should be true):", test7())
    print("Test 8 (Should be 'y': True, 'x': True):", test8())
    print("Test 9 (Should be true):", test9())
    print("Test 10 (Should be false):", test10())
    print("Test 11 (Should be true):", test11())
    print("Test 12 (Should be false):", test12())
    print("Test 13 (Should be {'z': True, 'y': True, 'x': True}):", test13())
    print("Test 14 (Should be true):", test14())
    print("Test 15 (Should be false):", test15())