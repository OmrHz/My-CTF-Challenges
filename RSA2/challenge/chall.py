from Crypto.Util.number import getPrime, bytes_to_long
from secret import FLAG
class RSAChallenge:
    def __init__(self, prime_bits=200):
        self.prime_bits = prime_bits
        self.p = getPrime(self.prime_bits)
        self.q = getPrime(self.prime_bits)
        self.n = self.p * self.q
        self.e = 0x10001  # Standard RSA public exponent (65537)
        
    def encrypt_flag(self, flag):
        flag_int = bytes_to_long(flag)
        self.ct = pow(flag_int, self.e, self.n)
        return self.ct
        
    def hint(self):
        self.N = 3*pow(self.p, 2) + 5*pow(self.q, 2) + 2*self.p*self.q - self.ct
        return self.N
        
    def output(self):
        print("ct:", self.ct)
        print("N:", self.N)

def main():
    challenge = RSAChallenge(prime_bits=200)
    challenge.encrypt_flag(FLAG)
    challenge.hint()
    challenge.output()

if __name__ == "__main__":
    main()
    
# ct: 389271138399689509182059643297539370637804419262475765296433755401842477574701477180248481393395091924716247706872421517
# N: 15876517952842231743882078565523390513475999015585623124726053622811042847436367020509246697786526386673329970500580002813