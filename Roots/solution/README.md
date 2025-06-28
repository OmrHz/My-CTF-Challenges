# Roots

## Write-up

Looking at how the prime `r` is generated:

```python 
while True:
    q = getPrime(2048)
    r = next_prime(q)
    if MIN < r - q < MAX:
        break
```
We see that `q` and `r` are close, which suggests a potential relation between n1 and n2. We derive the following equation:

$$
n_1 \cdot n_2 = p \cdot q \cdot (q + i) \cdot s = q \cdot s \cdot (p \cdot q + i \cdot p)
$$

Then:

$$
0 \equiv q \cdot s \cdot (p \cdot q + i \cdot p) \pmod{n_1 \cdot n_2}
$$

$$
0 \equiv p \cdot q + i \cdot p \pmod{p \cdot (q + i)}
$$

$$
0 \equiv n_1 + i \cdot p \pmod{p \cdot (q + i)}
$$

Solve script is [here](solve.sage)

## Flag

`shellmates{n3VEr_UnD3R3$tImatE_$m4LL_ro0ts!!}`


