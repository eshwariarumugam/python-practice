#count vowels in string
text=input("Enter string:")
count=0
for ch in text:
    if ch in "aeiouAEIOU":
         count+=1     
print("Count of vowels in string:",count) 
