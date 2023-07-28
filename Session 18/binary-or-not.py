def is_binary(number_str):
    # Iterate through each character in the string
    for char in number_str:
        # If any character is not '0' or '1', it's not a binary representation
        if char not in ('0', '1'):
            return False
    return True

def main():
    try:
        n = int(input("Enter a single integer n: "))
        if 0 <= n <= 30000:
            number_str = str(n)
            if is_binary(number_str):
                print(f"{number_str} is a valid binary representation.")
            else:
                print(f"{number_str} is not a binary representation.")
        else:
            print("Invalid input. The integer should be between 0 and 30000.")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()
