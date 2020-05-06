n = 10000
lst = [2]
k = 3
while len(lst) < n:
    f = 0
    for a in lst:
        if k % a == 0:
            f = 1
            break
    if f == 0:
        lst.append(k)
    k += 2
print(lst[-1])            
