x = 'yes'

while x == 'yes':
    amount = float(input("Enter the total purchase amount: "))
    
    if amount > 5000:
        discount = amount * 0.10
    else:
        discount = amount * 0.05
    
    price = amount - discount
    print(f"Initial Purchase Amount: {amount:.2f}")
    print(f"Discount: {discount:.2f}")
    print(f"Final Price: {price:.2f}")
    
    x = input("Do you want to try again? (yes/no): ").lower()

print("Thank you!")
