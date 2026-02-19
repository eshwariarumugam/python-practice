#armstrong
n=int(input("Enter number:"))  
if n<0:
    print("Not a armstrong number")
else :
    c=0
    temp=n   
    
    while temp>0: 
        c+=1
        temp=temp//10
    temp=n 
    total=0   
    while temp>0:
        d=temp%10
        total=total+d**c
        temp=temp//10
if total==n:        
    print("Armstrong Number:")   
else:
    print("Not a armstrong number")
