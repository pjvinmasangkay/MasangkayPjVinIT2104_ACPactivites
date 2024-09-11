x = input("Enter a string: ")

vowels = "aeiouAEIOU"  
result = []  

for char in x:
    if char in vowels:  
        result.append(char)

print(result)
