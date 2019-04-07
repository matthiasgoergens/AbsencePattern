from hypothesis import given
import hypothesis.strategies as st


def cart(x, y):
    for ix in x:
        for iy in y:
            yield (ix + iy)

def allPatterns(n, s):
    r = ['']
    for _ in range(n):
        r = cart(r, s)
    return r

print (list (allPatterns(3, "01")))
