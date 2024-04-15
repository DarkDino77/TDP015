import itertools

class Exp(object):
    """A Boolean expression."""

    def __init__(self, sym, *sexps):
        self.sym = sym
        self.sexps = sexps

    def value(self, assignment):
        raise NotImplementedError("This method should be overridden by subclasses.")

    def variables(self):
        variables = set()
        for sexp in self.sexps:
            variables |= sexp.variables()
        return variables

class Var(Exp):
    """A variable."""

    def __init__(self, sym):
        super().__init__(sym)

    def value(self, assignment):
        return assignment[self.sym]

    def variables(self):
        return {self.sym}

class Nega(Exp):
    """Logical not."""

    def __init__(self, sexp):
        super().__init__('¬', sexp)

    def value(self, assignment):
        return not self.sexps[0].value(assignment)

    def variables(self):
        return self.sexps[0].variables()

class Conj(Exp):
    """Logical and."""

    def value(self, assignment):
        return all(sexp.value(assignment) for sexp in self.sexps)

class Disj(Exp):
    """Logical or."""

    def __init__(self, *sexps):
        super().__init__('∨', *sexps)

    def value(self, assignment):
        return any(sexp.value(assignment) for sexp in self.sexps)

class Impl(Exp):
    """Logical implication."""

    def __init__(self, sexp1, sexp2):
        super().__init__('→', sexp1, sexp2)

    def value(self, assignment):
        return not self.sexps[0].value(assignment) or self.sexps[1].value(assignment)

class Equi(Exp):
    """Logical equivalence."""

    def __init__(self, sexp1, sexp2):
        super().__init__('↔', sexp1, sexp2)

    def value(self, assignment):
        return self.sexps[0].value(assignment) == self.sexps[1].value(assignment)

def assignments(variables):
    for values in itertools.product([True, False], repeat=len(variables)):
        yield dict(zip(variables, values))

def satisfiable(exp):
    for assignment in assignments(exp.variables()):
        if exp.value(assignment):
            return assignment
    return False

def tautology(exp):
    return all(exp.value(assignment) for assignment in assignments(exp.variables()))

def equivalent(exp1, exp2):
    return all(exp1.value(assignment) == exp2.value(assignment) for assignment in assignments(exp1.variables() | exp2.variables()))

def test1():
    a = Var('a')
    b = Var('b')
    c = Var('c')
    exp1 = Impl(Impl(a, b), c)
    exp2 = Conj(Disj(a, c), Disj(Nega(b), c))
    return equivalent(exp1, exp2)

if __name__ == "__main__":
    print("Test 1:", test1())
    # More tests can be added here.
