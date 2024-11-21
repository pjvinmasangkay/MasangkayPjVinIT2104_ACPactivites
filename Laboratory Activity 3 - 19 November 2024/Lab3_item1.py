def lib(roman):
    values= {
        'i': 1, 'v': 5, 'x': 10, 'l': 50, 'c': 100, 
        'd': 500, 'm': 1000, 'I': 1, 'V': 5, 'X': 10, 
        'L': 50, 'C': 100, 'D': 500, 'M': 1000
    }

    roman = roman.lower()

    total = 0
    prev_value = 0

    for char in reversed(roman):
        if char not in values:
            print(f"Invalid character: {char}")
            return None

        current_value = values[char]

        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value

        prev_value = current_value

    return total

def main():
    roman_input = input("Enter a Roman numeral: ")

    result = lib(roman_input)

    if result is not None:
        print(f"The integer value of {roman_input} is {result}.")
    else:
        print("Please enter a valid Roman numeral.")

if __name__ == "__main__":
    main()
