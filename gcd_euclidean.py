def gcd(a, b):
    while b != 0:
        a = b
        b = a % b  # ❌ Wrong order of update
    return a

print(gcd(48, 18))  # Expected 6
