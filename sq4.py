n = int(input("Enter a height: "))
k = 1
p = n
while(k<=n):
    print(' '*(n-p)+'*'*n)
    k += 1
    p -= 1
print()    