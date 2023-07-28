def rotate_matrix_90_clockwise(matrix):
    # Transpose the matrix
    transposed_matrix = list(zip(*matrix))

    # Reverse each row to get the 90 degrees clockwise rotated matrix
    rotated_matrix = [row[::-1] for row in transposed_matrix]

    return rotated_matrix

def print_matrix(matrix):
    for row in matrix:
        print(" ".join(str(num) for num in row))

if __name__ == "__main__":
    # Test case 1
    matrix1 = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    print("Original Matrix:")
    print_matrix(matrix1)

    rotated_matrix1 = rotate_matrix_90_clockwise(matrix1)
    print("\nRotated Matrix:")
    print_matrix(rotated_matrix1)

    # Test case 2
    matrix2 = [
        [11, 22, 33],
        [44, 55, 66],
        [77, 88, 99]
    ]

    print("\nOriginal Matrix:")
    print_matrix(matrix2)

    rotated_matrix2 = rotate_matrix_90_clockwise(matrix2)
    print("\nRotated Matrix:")
    print_matrix(rotated_matrix2)
