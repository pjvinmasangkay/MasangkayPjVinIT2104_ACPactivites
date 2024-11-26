def main():
    try:
        size = int(input("Enter the size of the array: "))
        
        arr = []
        print("Enter the elements of the array:")
        
        for i in range(size):
            element = float(input())
            arr.append(element * 5)  
        
        x = int(input("Enter the index of the element to print: "))
        
        print(f"Element at index {x}: {arr[x]:.2f}")
    
    except IndexError:
        print(f"Index {x} is invalid.")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()
