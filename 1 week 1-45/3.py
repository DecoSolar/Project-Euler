import math

k = 600851475143
for i in range(0, 600851475143):
    if 600851475143 % (k-i) == 0:
        if math.gcd(1, k-i) == 1:
            print(k-i)
            break
