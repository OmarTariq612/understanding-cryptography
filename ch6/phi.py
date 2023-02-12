from math import gcd


def phi_brute_force(m: int) -> int:
    count = 0
    for i in range(m):
        if gcd(i, m) == 1:
            count += 1
    return count

print(phi_brute_force(15))
print(phi_brute_force(26))
