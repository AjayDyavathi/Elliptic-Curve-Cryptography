class DiffieHellman():
    '''Elliptic Curve Diffie Hellman(ECDH) Key Exchange'''

    def __init__(self, curve, gen, private):
        self.curve = curve
        self.gen = gen
        self.private = private

    def calc_public(self):
        '''Calculates public by multiplying generator with private integer'''
        return self.curve.multiply(self.gen, self.private)

    def calc_shared_key(self, public):
        '''calculates common shared key by multiplying our private with recieved public point'''
        return self.curve.multiply(public, self.private)


# last paramerter(n) must be a prime
curve = EC(1, 15, 19)


# ELLIPTIC CURVE DIFFIE HELLMAN:
gen = curve.generator()     # generator method returns a random point from list of generators
print('generator:', gen)

# PARTY 1
priv1 = 123         # a secret integer for party1
party1 = DiffieHellman(curve, gen, priv1)
pub1 = party1.calc_public()
print('Party1 public point:', pub1)


# PARTY 2
priv2 = 657         # a secret integer for party2
party2 = DiffieHellman(curve, gen, priv2)
pub2 = party2.calc_public()
print('Party2 public point:', pub2)


key_at_party1 = party1.calc_shared_key(pub2)
key_at_party2 = party2.calc_shared_key(pub1)

print()
assert key_at_party1 == key_at_party2
print('Party1 and Party2 shared a common key', key_at_party1)
