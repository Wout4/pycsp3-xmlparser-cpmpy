from pycsp3 import *

n, d = data.nDominos, data.nValues

# x[i] is the value of the ith domino
x = VarArray(size=n, dom=range(d))

if not variant():
    satisfy(
        AllEqual(x),

        (x[0] + 1 == x[- 1]) | ((x[0] == x[- 1]) & (x[0] == d - 1))
    )

elif variant("table"):
    satisfy(
        [(x[i], x[i + 1]) in {(a, a) for a in range(d)} for i in range(n - 1)],

        (x[0], x[- 1]) in {(a + 1, a) for a in range(d - 1)} | {(d - 1, d - 1)}
    )


# TODO: would it be possible to extend the code so as be able to to write : x[0] == x[- 1] == v - 1? this is not obvious