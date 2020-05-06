
A = [[[] for i in range (3)] for i in range(3)]

for i in range(3):
    for j in range(3):
        number = (int(input("Enter no. of elements in matrix A:")))
        A[i][j] = number
print(A)        