# pyramid pattern
rows=int(input("Enter the number of rows:")) 
for i in range (1,rows+1):
    for space in range(rows-i):
        print(" ",end=" ")
    for j in range(i-1):
        print("*",end=" ")
    print( )   
