#find()
text="python programming"
print(text.find("python"))
print(text.find("programming"))
print(text.find("c"))

#count()
text="apple"
print(text.count("a"))
print(text.count("p"))
print(text.count("s"))

#isupper()
word="banana"
print(word.isupper())

#islower
word="Python"
print(word.islower())

#isalpha()
print("python".isalpha())
print("python3".isalpha())
print("python 1".isalpha())

#isdigit()
print("123".isdigit())
print("123.5".isdigit())
print("2 3a".isdigit())

#isalnum()
print("python 123".isalnum())
print("python3".isalnum())

#isspace()
print(" ".isspace())
print("a".isspace())

#startswith()
text="python.py"
print(text.startswith("py"))

#endswith()
text="python.py"
print(text.endswith(".py"))

#split()
text="rose,jasmine,lily"
flower=text.split(",")
print(flower)

#join()
text=["I","am","happy"]
sentence=" ".join(text)
print(sentence)

