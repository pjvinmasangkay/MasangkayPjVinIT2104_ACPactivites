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
    num = int(input("Enter a number: "))
    
    if pnumber(num):
        print(f"{num} is a perfect number.")
    else:
        print(f"{num} is not a perfect number.")

if __name__ == "__main__":
    main()
