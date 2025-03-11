def main():
    try:
        number = int(input(""))
        if number > 25:
            print("Error")
        else:
            while number <= 25:
                print(number)
                number += 1
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()