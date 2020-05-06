import math

a = int(input("Enter a value a:"))
b = int(input("Enter a value b:"))
c = int(input("Enter a vlaue c:"))
d = b * b - 4 * a * c
if d < 0:
    print("ROOTS are imaginery")

else:
    root1 = (b - math.sqrt(d)) / (2.0 * a)
    root2 = (b + math.sqrt(d)) / (2.0 * a)
    print("ROOT1 = ", root1)
    print("ROOT2 = ", root2)