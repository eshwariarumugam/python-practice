#Hollow triangle
rows=int(input("Enter rows: "))
for i in range(1,rows+1):
    for j in range(1,i+1):
        if j==1 or i==rows or j==i:
            print("*",end="")
        else:
            print(" ",end="")    
    print()    
    
