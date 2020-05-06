row = int(input("rows dalo:"))
n = row
while n >= 0:
    x = "*" * n
    y = " "*(row-n)
    print(y + x)
    n -= 1