def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # ✅ Correct simultaneous update
    return a

print(gcd(48, 18))  # Output: 6
