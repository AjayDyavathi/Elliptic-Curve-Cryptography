# Elliptic-Curve-Cryptography
Various Elliptic_Curve services

ECDH.py is an implementation of Elliptic Curve Diffie-Hellman Key exchange method.
The chosen curve for the implementation is (a=1, b=15, n=19), where curve equation looks like
 _y² = x³ + ax + b mod n_
 
 **Elliptic curve is always symmetric over X-axis**
 
 _Point-addition_:  
 * Draw a line through the two points(say a, b)
 * The line cuts the curve at another third point(say c)
 * The symmetric point over X-axis (which is negated) is the result of a+b (say d)
 * eg: a=(x1, y1), b=(x2, y2), c=(x3, y3), d = (x3, -y3) 
 
 _Point-multiplication_:
 
 * point-addition n times O(n) OR 
 * add_and_double method O(logn) 
 
 I'll update with ECDSA soon.
 
 Note: this code is for basic understanding, the parameters in real-life implementations are large.
