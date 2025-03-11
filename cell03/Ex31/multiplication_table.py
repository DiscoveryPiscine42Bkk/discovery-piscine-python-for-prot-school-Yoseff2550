def main():
    try:
        number = int(input(""))
        print(f"Multiplication table for {number}:")
        for i in range(1, 11): 
            print(f"{number} x {i} = {number * i}")
    
    except ValueError:
        print("Please enter a valid number.")
if __name__ == "__main__":
    main()
