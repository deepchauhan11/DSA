def spiral_traversal(matrix, n):
    result = []
    top = 0
    bottom = n - 1
    left = 0
    right = n - 1

    while len(result) < n * n:
        # Traverse from left to right
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        # Traverse from top to bottom
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        # Traverse from right to left
        for i in range(right, left - 1, -1):
            result.append(matrix[bottom][i])
        bottom -= 1

        # Traverse from bottom to top
        for i in range(bottom, top - 1, -1):
            result.append(matrix[i][left])
        left += 1

    return result


def main():
    n = int(input())
    matrix = []

    for _ in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)

    result = spiral_traversal(matrix, n)
    print(" ".join(map(str, result)))


if __name__ == "__main__":
    main()
