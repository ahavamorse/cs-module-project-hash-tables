import itertools

"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6


# Your code here

def equal_sum_diff(a, b, c, d):
    a_result = f(a)
    b_result = f(b)
    c_result = f(c)
    d_result = f(d)

    if a_result + b_result == c_result - d_result:
        print(f'f({a}) + f({b}) = f({c}) - f({d})   {a_result} + {b_result} = {c_result} - {d_result}')


def all_equal_sum_diff(q):
    possibilities = list(itertools.product(q, repeat=4))
    for a, b, c, d in possibilities:
        equal_sum_diff(a, b, c, d)


all_equal_sum_diff(q)
