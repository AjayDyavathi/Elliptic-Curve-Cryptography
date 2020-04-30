from EC import EC


class ElGamal():
    '''ElGamal Encryption with Elliptic Curves'''

    def __init__(self, ec):
        self.ec = ec
        self.gen = self.ec.generator()

    def get_public(self, priv):
        return self.ec.multiply(self.gen, priv)

    def encrypt(self, message, public, rand):
        '''This is done on the other party side, where you send your
        key to other party. This is how they encrypt a message, where
        message is a point on elliptic curve'''

        # EPHEMERAL KEY - Temporary Key for Session
        Ke = self.ec.multiply(self.gen, rand)

        # MASKING KEY - Actual Key for encryption
        Km = self.ec.multiply(public, rand)

        # ECNRYPTION
        cipher = self.ec.point_addition(message, Km)

        return (Ke, cipher)

    def decrypt(self, cipher, private):
        '''This is done on owner side, where he receives cipher as a point on curve'''

        Ke, cipher_point = cipher

        # Calculating MASKING key from Ke
        Km = self.ec.multiply(Ke, private)

        # Inverse Masking key
        iKm = self.ec.negate(Km)

        plain = self.ec.point_addition(cipher_point, iKm)
        return plain


# last paramerter(n) must be a prime
curve = EC(1, 15, 19)

eg = ElGamal(curve)

private = 143
pub = eg.get_public(private)
print('Public key point:', pub)

message = curve.generator()  # this will be some point ON CURVE serves us as msg
print('Message', message)

random_number = 12  # select a new random number for every session of encryption
cipher = eg.encrypt(message, pub, random_number)
print('encrypted:', cipher)

plain = eg.decrypt(cipher, private)
print('decrypted:', plain)

assert message == plain
