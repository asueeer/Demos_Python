import math
import random

S_total = 16
N = 100000
N1 = 0

for i in range(N):
    x = random.uniform(0,4)
    y = random.uniform(0,4)

    if (x * x + y * y > 4 * 4) & ((x - 4) * (x - 4) + y * y < 4 * 4) & (
            (x - 4) * (x - 4) + (y - 4) * (y - 4) < 4 * 4) & (
            x * x + (y - 4) * (y - 4) > 4 * 4):
        N1 = N1 + 1
    else:
        pass

# print(N1)
S = N1 / N * S_total * 4

print("Method of MengTeKaLuo:")
print(16- S)
print("Precise result:")
S_precise = 32 / 3 * 3.141592653 + 16 * pow(3, 1 / 2) - 48
print(S_precise)