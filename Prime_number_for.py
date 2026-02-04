#check is a number is prime or not
n=int(input("Enter the number:"))
if n>1:
    is_prime=True
    for i in range(2,n//2+1):
        if n%i==0:
            is_prime=False
            break
    if is_prime:
        print("prime number")       
    else:
        print("Not a prime number")
else:
    print("not a prime number") 
