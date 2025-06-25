# log.py
# Demonstration of different types of operators in Python

a = 10
b = 3

# Arithmetic Operators
print("Arithmetic Operators:")
print(f"a + b = {a + b}")
print(f"a - b = {a - b}")
print(f"a * b = {a * b}")
print(f"a / b = {a / b}")
print(f"a % b = {a % b}")
print(f"a ** b = {a ** b}")
print(f"a // b = {a // b}")

# Assignment Operators
print("\nAssignment Operators:")
c = a
print(f"c = {c}")
c += b
print(f"c += b: {c}")
c -= b
print(f"c -= b: {c}")
c *= b
print(f"c *= b: {c}")
c /= b
print(f"c /= b: {c}")

# Comparison Operators
print("\nComparison Operators:")
print(f"a == b: {a == b}")
print(f"a != b: {a != b}")
print(f"a > b: {a > b}")
print(f"a < b: {a < b}")
print(f"a >= b: {a >= b}")
print(f"a <= b: {a <= b}")

# Logical Operators
print("\nLogical Operators:")
print(f"(a > 5) and (b < 5): {(a > 5) and (b < 5)}")
print(f"(a < 5) or (b < 5): {(a < 5) or (b < 5)}")
print(f"not(a == b): {not(a == b)}")

# Bitwise Operators
print("\nBitwise Operators:")
print(f"a & b: {a & b}")
print(f"a | b: {a | b}")
print(f"a ^ b: {a ^ b}")
print(f"~a: {~a}")
print(f"a << 1: {a << 1}")
print(f"a >> 1: {a >> 1}")

# Membership Operators
print("\nMembership Operators:")
lst = [1, 2, 3, 10]
print(f"a in lst: {a in lst}")
print(f"b not in lst: {b not in lst}")

# Identity Operators
print("\nIdentity Operators:")
x = 5
y = 5
z = [5]
print(f"x is y: {x is y}")
print(f"x is not z[0]: {x is not z[0]}")