# TDP015 Programmeringsuppgift N
# Numeriska metoder
# Skelettkod

# Er uppgift �r att implementera Newtons metod f�r att approximera
# nollst�llen till en funktion och att sedan till�mpa denna
# implementation f�r att l�sa tre numeriska ber�kningsproblem. En
# beskrivning av metoden hittar du h�r:
#
# https://sv.wikipedia.org/wiki/Newtons_metod

# ## Del 1

# ### Problem 1
#
# Implementera ett steg av Newton-approximationen.


def newton_one(f, f_prime, x0):
    """Compute the next Newton approximation to a root of the function `f`,
    based on an initial guess `x0`.

    Args:
        f: A float-valued function.
        f_prime: The function's derivative.
        x0: An initial guess for a root of the function.

    Returns:
        The next Newton approximation to a root of the function `f`, based on
        the initial guess `x0`.
    """
    # TODO: Replace the next line with your own code.
    return 0.0


# ### Problem 2
#
# Implementera en fullst�ndig Newton-approximation.


def newton(f, f_prime, x0, n_digits=6):
    """Compute the Newton approximation to a root of the function `f`, based
    on an initial guess `x0`.

    Args:
        f: A float-valued function.
        f_prime: The function's derivative.
        x0: An initial guess for a root of the function.
        n_digits: The desired precision of the approximation.

    Returns:
        A pair consisting of the Newton approximation to a root of the
        function `f` and the number of iterations needed to reach numerical
        stability. The precision of the approximation should be the specified
        number `n_digits` of digits after the decimal place. That is, the
        iterative process should end when the approximation does not alter the
        first `n_digits` after the decimal place.
    """
    # TODO: Replace the next line with your own code.
    return 0.0, 0


# ## Del 2

# ### Problem 3
#
# Anv�nd din kod f�r att approximera nollst�llet av funktionen
#
# f(x) = x^3 - x + 1
#
# Ange Python-funktioner `f` och `f_prime` och ett l�mpligt startv�rde `x0`
# och skriv ut ert numeriska resultat inklusive antalet iterationer.
# Noggrannheten ska vara sex siffror efter kommat.


def problem3():
    # TODO: Replace the following lines with your own code.
    f = lambda x: 0.0
    f_prime = lambda x: 1.0
    x0 = 0.0
    a, i = newton(f, f_prime, x0)
    print("approximation: {:.6f}, number of iterations: {}".format(a, i))


# ### Problem 4
#
# Anv�nd er kod f�r att approximativt ber�kna den femte roten ur 5. B�rja med
# att ange den funktion vars nollst�lle ni vill approximera. Forts�tt sedan
# som i f�reg�ende uppgift.


def problem4():
    # TODO: Replace the following lines with your own code.
    f = lambda x: 0.0
    f_prime = lambda x: 1.0
    x0 = 0.0
    a, i = newton(f, f_prime, x0)
    print("approximation: {:.6f}, number of iterations: {}".format(a, i))


# ### Problem 5
#
# Ange en funktion och tv� olika startv�rden s�dana att Newtons metod r�knar
# ut tv� helt olika approximationer.


def problem5():
    # TODO: Replace the following lines with your own code.
    f = lambda x: 0.0
    f_prime = lambda x: 1.0
    x01 = 0.0
    x02 = 0.0
    a1, _ = newton(f, f_prime, x01)
    a2, _ = newton(f, f_prime, x02)
    print("approximation 1: {:.6f}".format(a1))
    print("approximation 2: {:.6f}".format(a2))


if __name__ == "__main__":
    print("Problem 3")
    problem3()

    print("")
    print("Problem 4")
    problem4()

    print("")
    print("Problem 5")
    problem5()
