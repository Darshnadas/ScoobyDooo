n = int(input("Enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        if i == 1 or i == n:
            print("*", end = "")
        else:
            print("*", " "*(n-2), "*")  
print()          
