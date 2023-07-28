def find_missing_number(a, n):
    # Calculate XOR of all numbers from 1 to n
    xor_all = 0
    for i in range(1, n + 1):
        xor_all ^= i

    # Calculate XOR of all elements in the array a[]
    xor_a = 0
    for num in a:
        xor_a ^= num

    # XOR of xor_all and xor_a gives the missing number
    missing_number = xor_all ^ xor_a
    return missing_number

# Test cases
test_cases = [
    ([3, 6, 1, 5, 4], 6),
    ([8, 3, 2, 1, 5, 4, 7], 8),
    ([3, 2, 4, 5], 5)
]

for a, n in test_cases:
    result = find_missing_number(a, n)
    print(f"The missing number in array {a} (n={n}) is: {result}")
