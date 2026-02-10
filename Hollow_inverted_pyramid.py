#Hollow inverted  pyramid   
rows=int(input("Enter rows: "))
for i in range(rows,0,-1):
    for space in range(rows-i):
        print(" ",end=" ")
    for j in range(1,2*i):
        if j==1  or j==2*i-1 or i==rows:
            print("*",end=" ")
        else:
            print(" ",end=" ")    
    print()     
            
