from Crypto.Util.number import *
from sympy.abc import x, y, t
from sympy.solvers.diophantine.diophantine import diop_quadratic
ct= 389271138399689509182059643297539370637804419262475765296433755401842477574701477180248481393395091924716247706872421517
N=15876517952842231743882078565523390513475999015585623124726053622811042847436367020509246697786526386673329970500580002813
solve = diop_quadratic(3*x**2 + 5*y**2 + 2*x*y - ct - N, t)
print('solved')

for p, q in solve:
    p, q = int(p), int(q)
    if isPrime(p) and isPrime(q):
        phi = (p-1)*(q-1)
        n=p*q
        d = inverse(0x10001, phi)
        pt=pow(ct, d, n)
        print(long_to_bytes(pt)) # shellmates{Qu4DRat1c_d10pH4NTinE_3Qu4tioN}
        break