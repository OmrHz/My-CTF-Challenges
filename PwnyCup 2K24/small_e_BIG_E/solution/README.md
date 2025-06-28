# Challenge: 
small_e_BIG_E
## Write-up

### Small_e Attack

When the public exponent `e` is small, the encryption becomes weak. If the message `m` is such that \( m^e < N \), we can directly compute the eth root of the ciphertext to recover the message.

For example, if \( e = 3 \), the message can be obtained by calculating:
$$m=\sqrt[3]{c}$$

If \( m^e > N \), we can progressively add multiples of \( N \) until the cube root yields a valid message:
$$m=\sqrt[3]{c+kN}$$
### BIG_E Attack (Wiener's Attack)
Wiener's Attack  attempt to guess the decryption exponent `d` when `e` is large, as `d` is necessarily small as a result.  
you can read more [here](https://en.wikipedia.org/wiki/Wiener%27s_attack)

check [solve.py](solve.py)
## Flag

`shellmates{Y0u_wanna_Lo$e_Small_I_WANNA_w1n_bI11111iG}`
