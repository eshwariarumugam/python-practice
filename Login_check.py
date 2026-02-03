#Login check
username=input("Enter username:").lower()
password=int(input("Enter password:"))
if username=="admin" and password==1234:
    print("Login successful")
else:
    print("Login failed")
