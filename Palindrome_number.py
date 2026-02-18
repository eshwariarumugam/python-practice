#paindrome
n=int(input("Enter number:"))
if n<0:
    print("Not a palindrome")
temp=n
rev=0
while n>0:
    d=n%10
    rev=rev*10+d
    n=n//10
if temp==rev:
    print("palindrome")
else:
    print("Not a palindrome")        
