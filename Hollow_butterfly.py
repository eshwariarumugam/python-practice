rows=int(input("Enter number of rows: "))

for i in range(1,rows+1):
    for j in range(1,i+1):
        if j==i or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    for space in range(2*(rows-i)):
        print(" ",end="")
    for j in range(1,i+1):
        if j==i or j==1:
            print("*",end="")
        else:
            print(" ",end="")    
        
    print( )
for i in range(rows-1,0,-1):
    for j in range(1,i+1):
        if j==i or j==1:
            print("*",end="")
        else:
            print(" ",end="")
    for space in range(2*(rows-i)):
        print(" ",end="")
    for j in range(1,i+1):
        if j==i or j==1:
            print("*",end="")
        else:
            print(" ",end="")   
    print()         
            
