#Basics
name="Eshwari"
print(name)              #original name
print(name.upper())      #uppercase
print(name.lower())      #lowercase
print(len(name))      #length of string

#Indexing &slicing
text="pythonprogramming"
print(text[0])          #First character
print(text[-1])         #Last character
print(text[0:6])        #first 6 character
print(text[6:])         #after 6th character

#string cleaning
text=input("Enter text: ")
print(text)              #original
print(text.strip())      # without space
print( text.replace("world","python"))  #replace works only if the word exist

# Strings are immutable because once created, their characters
# cannot be changed. Any modification creates a new string.

# Accessing an invalid index raises an IndexError.
