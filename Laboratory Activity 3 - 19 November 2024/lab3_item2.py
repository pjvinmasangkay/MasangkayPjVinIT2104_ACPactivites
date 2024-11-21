def pnumber(number):
    divisors_sum = 0
    
    for i in range(1, number):
        if number % i == 0:  
            divisors_sum += i

    if divisors_sum == number:
        return True
    else:
        return False

def main():
    try:
     num = int(input("Enter a number: "))
    
     if pnumber(num):
         print(f"{num} is a perfect number.")
     else:
         print(f"{num} is not a perfect number.")
         
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
