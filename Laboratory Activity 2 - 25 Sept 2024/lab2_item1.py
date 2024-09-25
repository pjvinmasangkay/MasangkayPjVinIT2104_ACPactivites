x = input("Enter an integer: ")

if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
    num = x
    if num == num[::-1]:
        print("Palindrome")
    else:
        print("Not a Palindrome")
