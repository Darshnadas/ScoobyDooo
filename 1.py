amt = float(input("Enter a amount:"))
inrate = float(input("Enter an interest rate:"))
period = float(input("Enter a period:"))

year = 1
value = 0

while year<= period:
    value = amt+(inrate*amt)
    print("Year %d  Rs. %.2f" %(year,value))
    amt = value
    year = year+1
