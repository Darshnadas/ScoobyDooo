n = int(input("Enter a height you want:"))
k = 1
while(k<=n):
    if k == 1 or k == n:
        print(' '*(n-k)+'*'*n)
        k += 1
    else:
        print(' '*(n-k)+'*'+' '*(n-2)+'*')
        k += 1
print()


