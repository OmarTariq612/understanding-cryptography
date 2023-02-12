from typing import Dict


def extended_iterative(a: int, b: int) -> Dict[str, int]:
    """a >= b"""
    if b == 0 or a % b == 0:
        return {"gcd": b, "s": 0, "t": 1}

    s0, s1 = 1, 0
    t0, t1 = 0, 1
    r0, r1 = a, b

    while True:
        q = r0 // r1
        r0, r1 = r1, r0 % r1
        s0, s1 = s1, s0 - q * s1
        t0, t1 = t1, t0 - q * t1
        if r1 == 0:
            break
    return {"gcd": r0, "s": s0, "t": t0}


print(extended_iterative(973, 301))
print(extended_iterative(973, 973))
print(extended_iterative(25, 5))
print(extended_iterative(25, 5))
