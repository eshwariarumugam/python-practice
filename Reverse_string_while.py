#reverse a string    
text = input("Enter string: ")
i = len(text) - 1

while i >= 0:
    print(text[i], end="")
    i -= 1   
