# TDP015 Programming Assignment 2
# Recursion
# Skeleton Code

# Do not use any imports!

# In this assignment you are asked to implement functions on *nested
# pairs*. The set of nested pairs is defined recursively:
#
# 1. The empty tuple () forms a nested pair.
#
# 2. If a and b are nested pairs, then the tuple (a, b) forms a nested
#    pair.
#
# Here are some examples of nested pairs sorted by their *degree*. The
# degree of a nested pair is the number of empty tuples contained in it.
#
# degree 1 (1 pair):
#
# ()
#
# degree 2 (1 pair):
#
# ((), ())
#
# degree 3 (2 pairs):
#
# ((), ((), ()))
# (((), ()), ())
#
# degree 4 (5 pairs):
#
# ((), ((), ((), ())))
# ((), (((), ()), ()))
# (((), ()), ((), ()))
# (((), ((), ())), ())
# ((((), ()), ()), ())
#
# The following sequence gives the number of nested pairs with degrees
# 1, 2, 3, ...:
#
# 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796, 58786, 208012, 742900,
# 2674440, 9694845, 35357670, 129644790, 477638700, 1767263190, ...

# ## Problem 1
#
# Implement a function nested_pairs() that yields all nested pairs
# with a specified degree. Each nested pair should be yielded exactly
# once. For example, nested_pairs(4) should yield the 5 nested pairs
# listed above. Use recursion. Test your function by counting the
# number of nested pairs yielded by it and comparing against the
# sequence of numbers given above.

def nested_pairs(n):
    """Yield all nested pairs with degree *n*."""
    if n == 1:
        yield ()
    else:    
        for i in range(1,n):
            for a in nested_pairs(i):
                for b in nested_pairs(n-i):
                    yield (a,b)
    pass

def test_nested_pairs():
    catalan_numbers = [1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, 16796]

    for degree, expected_count in enumerate(catalan_numbers, start=1):
        generated_pairs = list(nested_pairs(degree))
        
        count_generated = len(generated_pairs)
        
        if count_generated != expected_count:
            print(f"Test failed for degree {degree}: expected {expected_count}, but got {count_generated}")
            return False
        else:
            print(f"Test passed for degree {degree}: {count_generated} pairs generated as expected.")
    
    print("All tests passed!")
    return True

#test_nested_pairs()



# ## Problem 2
#
# Implement a function count_nested_pairs() that counts the number of
# nested pairs with a specified degree. A naive implementation of this
# function would call the nested_pairs() function from Problem 1. This
# is not what you are supposed to do! Instead, try to come up with a
# solution that counts the number of nested pairs without generating
# them. There is a way to solve this problem using a formula; but your
# solution should use recursion. Test your implementation by comparing
# your numbers to the numbers that you got above. What is the maximal
# degree for which you can compute the number of nested pairs in under
# one minute?

def count_nested_pairs(n):
    """Count the number of nested pairs with degree *n* using recursive approach."""
    if n == 1:
        return 1
    else:
        count = 0
        for i in range(1, n):
            count += count_nested_pairs(i) * count_nested_pairs(n - i)
        return count



def check_count_nested_pairs(n):
    for degree in range(1,n):
        expected_count = count_nested_pairs(degree)
        generated_pairs = list(nested_pairs(degree))
        
        count_generated = len(generated_pairs)
        
        if count_generated != expected_count:
            print(f"Test failed for degree {degree}: expected {expected_count}, but got {count_generated}")
            return False
        else:
            print(f"Test passed for degree {degree}: {count_generated} pairs generated as expected.")
    
    print("All tests passed!")
    return True

#check_count_nested_pairs(16)

def test_count_nested_pairs(n):
    counted = count_nested_pairs(n)
    print("Pairs: " + str(counted))
    return counted

#test_count_nested_pairs(20)
# We calculated test_count_nested_pairs(20) in under one minute.

    


# ## Problem 3
#
# Because it uses recursion, the function that you implemented in
# Problem 2 will call itself many times, and many times with the same
# argument. One way to speed things up is to cache the results of
# these calls. This strategy is called *memoization*.
#
# The idea is the following: All recursive calls of the function get
# access to a common cache in the form of a dictionary. Before a
# recursive call computes the number of nested pairs of a given degree
# *n*, it first checks whether that number is already stored in the
# cache. If yes, then the recursive call simply returns that
# value. Only if the value has not already been cached, the recursive
# call starts a computation on its own; but then it stores the result
# of that computation in the common cache, under the key *n*, so that
# subsequent calls will not have to recompute it.
#
# Write a function count_nested_pairs_memoized() that implements this
# idea. Test your implementation as above. How long does it take you to
# compute the number of nested pairs for the maximal degree that you
# could do in under one minute in Problem 2?

cache = {}

def count_nested_pairs_memoized(n):
    """Count the number of nested pairs with degree *n* using memoization."""
    if n in cache:
        return cache[n]
    if n == 1:
        cache[n] = 1
    else:
        count = 0
        for i in range(1, n):
            count += count_nested_pairs_memoized(i) * count_nested_pairs_memoized(n - i)
        cache[n] = count
    return cache[n]


def check_count_nested_pairs_memoized(n):
    for degree in range(1, n):
        expected_count = count_nested_pairs_memoized(degree)

        if expected_count != count_nested_pairs(degree):
            print(f"Test failed for degree {degree}: expected {expected_count}, got {count_nested_pairs(degree)}")
            return False
        else:
            print(f"Test passed for degree {degree}: {expected_count} pairs counted as expected.")
    
    print("All tests passed!")
    return True


#check_count_nested_pairs_memoized(16)

def test_count_nested_pairs_memoized(n):
    counted = count_nested_pairs_memoized(n)
    print("Pairs: " + str(counted))
    return counted

test_count_nested_pairs_memoized(20)
# We could calculate 20 degrees of nested pairs in < 1 second using memoized calls.