x = int(input("Enter an integer: "))

num = str(x)
if num == num[::-1]:
    print("Palindrome")
else:
    print("Not a Palindrome")
