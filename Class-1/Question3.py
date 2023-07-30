def main():
    ascii_values = [68, 98, 120]

    print("Output:")
    for value in ascii_values:
        char = chr(value)
        print(f"{value}-> {char}")

if __name__ == "__main__":
    main()
