# Inverted Pyramid
rows=int(input("Enter number of rows:"))
for i in range(rows,0,-1):
    for space in range(rows-i):
        print(" ",end="")
    for j in range(2*i-i):
        print("*",end=" ")
    print()      
