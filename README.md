# Elliptic-Curve-Cryptography
Various Elliptic_Curve services

ECDH.py is an implementation of Elliptic Curve Diffie-Hellman Key exchange method.
The chosen curve for the implementation is (a=1, b=15, n=19), where curve equation looks like
 _y² = x³ + ax + b mod n_
 
 **Elliptic curve is always symmetric over X-axis**
 
 How to add two points on an elliptic curve(called as point-addition):  
 * Draw a line through the two points(say a, b)
 * The line cuts the curve at another third point(say c)
 * The symmetric point over X-axis (which is negated) is the result of a+b (say d)
 * eg: a=(x1, y1), b=(x2, y2), c=(x3, y3), d = (x3, -y3) 
 
 This code has only Diffie-Hellman Key exchange for now,
 I'll update with DSA and ElGamal soon.
 
 Note: this code is for basic understanding, the parameters in real-life implementations are large.
