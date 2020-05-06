n = int(input("Enter a height: "))
k = 1
p = n
while(k<=n):
    if k == 1 or k == n:
        print(' '*(n-p)+'*'*n)
        k += 1
        p -= 1
    else:
        print(' '*(n-p)+'*'+' '*(n-2)+'*')
        k += 1
        p -= 1
print()            