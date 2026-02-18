#count number of digit
n=int(input("Enter number:"))
n=abs(n)
c=0
if n==0:
    c=1
else:
    while n>0:
        c+=1
        n=n//10
print(c)    
