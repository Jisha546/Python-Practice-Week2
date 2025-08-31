text=input("enter a word")
count=0
vowels="aeiou"
for char in text:
    if char in vowels:
        count+=1
print("vowels in word",count)