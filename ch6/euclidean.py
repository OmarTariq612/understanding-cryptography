def gcd_recursive(a: int, b: int) -> int:
    """a <= b"""
    if a == 0:
        return b
    if b % a == 0:
        return a
    return gcd_recursive(b % a, a)


def gcd_iterative(a: int, b: int) -> int:
    """it does not matter"""
    mn = min(a, b)
    mx = max(a, b)
    if mn == 0:
        return mx
    while mx % mn != 0:
        mn, mx = mx % mn, mn
    return mn


def lcm(a: int, b: int) -> int:
    return (a * b) // gcd_iterative(a, b)
