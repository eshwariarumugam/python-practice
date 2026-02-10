#Hollow Inverted triangle
rows=int(input("Enter rows: "))
for i in range(rows,0,-1):
    for j in range(1,i+1):
        if j==1 or j==i or i==rows:
            print("*",end="")
        else:
            print(" ",end="")    
    print()    
    
