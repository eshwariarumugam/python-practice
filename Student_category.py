#student category
age=int(input("Enter your age:"))
student=input("Are you a student(yes/no):").lower()
if student=="yes"and age<18:
    print("Student is minor")
elif student=="yes"and age>=18:
    print("Student is adult")
else:
    print("Not a student")    
