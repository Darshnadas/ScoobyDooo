Matrix = [[[]for r in range(3)]for c in range(3)]

for r in range(3):
    for c in range(3):
        n = (int(input("Enter an element in Matrix:")))
        Matrix[r][c] = n
print(Matrix)        