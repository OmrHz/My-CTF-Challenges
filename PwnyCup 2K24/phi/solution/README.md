# Challenge name
Phi_φ(n)
## Write-up
In this challenge, the modulus `N` has 16 factors, and one of them is a prime raised to the power of 3 (``p^3``), which is unusual for RSA since ``N`` is usually the product of two primes. This causes issues when calculating the Euler's totient (``φ(N)``), which is crucial for decryption. After some research [here](https://cp-algorithms.com/algebra/phi-function.html), we find the correct totient properties to resolve this.
#### 1. If `P` is prime, then : φ(p<sup>k</sup>) = p<sup>k</sup> - p<sup>k-1</sup> = p<sup>k-1</sup>(p - 1)
#### 2. If `a` and `b` are relatively prime, then : φ(a*b) =φ(a) * φ(b)
check [solve.py](solve.py)
## Flag
`shellmates{3A$Y_t0T1Ent_when_$aMe_OR_m4nY_PR1me$_4RE_u$ed}`
