def main():
    while True:
        try:
            number = int(input("Enter a number: "))
            break 
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    print(f"Multiplication table for {number}:")
    for i in range(1, 11):
        print(f"{number} x {i} = {number * i}")

if __name__ == "__main__":
    main()
