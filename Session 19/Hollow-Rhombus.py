def print_hollow_rhombus(n):
    if n < 1:
        return

    for i in range(n):
        # Print spaces before stars
        for j in range(n - i - 1):
            print(" ", end="")
        
        # Print the top and bottom rows of the rhombus
        if i == 0 or i == n - 1:
            for j in range(n):
                print("*", end="")
        else:
            # Print the sides of the rhombus
            for j in range(n):
                if j == 0 or j == n - 1:
                    print("*", end="")
                else:
                    print(" ", end="")
        print()

# Test cases
print("n = 5")
print_hollow_rhombus(5)

print("\nn = 8")
print_hollow_rhombus(8)

print("\nn = 3")
print_hollow_rhombus(3)
