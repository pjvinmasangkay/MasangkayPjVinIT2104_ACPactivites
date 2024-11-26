from Capybara import Capybara

list = [
    Capybara("Biscoff", "M", 5),
    Capybara("Den", "M", 3),
]

try:
    test_case = int(input("Enter the test case number: "))
    if 1 <= test_case <= len(list):
        selected_capybara = list[test_case - 1]
        print(
            f"Test Case {test_case}: Name: {selected_capybara.name}, "
            f"Gender: {selected_capybara.gender}, Age: {selected_capybara.age} years old"
        )
    else:
        print("Invalid test case number.")
except ValueError:
    print("Invalid input.")
