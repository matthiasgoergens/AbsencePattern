from hypothesis import given
import hypothesis.strategies as st


def cart(x, y):
    """Cartesian product with +"""
    for ix in x:
        for iy in y:
            yield (ix + iy)

def allPatterns(n, s):
    r = ['']
    for _ in range(n):
        r = cart(r, s)
    return r

bads = ["aa", "ala", "all", "lal", "lla", "lll"]

def isBad(s):
    return any(b in s for b in bads)

def allBad(bads, patterns):
    """Brute force, select only penalty patterns out of all patterns"""
    return (p
     for p in patterns
     if any(b in p for b in bads))
# print (list (allPatterns(3, "01")))
def numBad(n):
    """Brute force, number of penalty patterns"""
    return len(list(allBad(list(bads), allPatterns(n, "ola"))))


from collections import defaultdict, Counter
def numBad1(n):
    """Sort-of dynamic programming solution for number of penalty patterns"""
    nextD = Counter([''])
    # steps:
    for _ in range(n):
        nextD, d = Counter(), nextD
        for key in d:
            for l in 'ola':
                nextKey = l + key
                nextD[nextKey[:2]] += d[key] * (not isBad(nextKey))
    else:
        all = len('ola')**n
        good = sum(nextD.values())
        bad = all - good
        return bad

if __name__ == '__main__':
    # print(bads)
    # print(numBad(10))
    for i in range(21):
        print(i, numBad1(i))

