from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    """ needs bounds per direction left,right, up, down
        initially left=0, right=len(matrix[0]), up=0, down=len(matrix)
        i, j to control where to go
        first i=0, j=1, go right
        second i=1, j=0 go down
        third i=0, j=-1 go left
        fourth, i=-1, j=0 go up
        repeat until all the bounds are voliated

    """

    ans = []
    R, C = len(matrix), len(matrix[0])
    seen = [[False] * C for _ in range(R)]
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    i, j, di = 0, 0, 0
    dr, dc = moves[di]
    # iterate over every cell
    for _ in range(R * C):
        ans.append(matrix[i][j])
        seen[i][j] = True
        if not (0 <= i + dr < R and 0 <= j + dc < C) or seen[i + dr][j + dc]:
            di = (di + 1) % 4
            dr, dc = moves[di]
        i += dr
        j += dc
    return ans


def rotate(matrix):
    length = len(matrix)

    for i in range(length // 2):  # layer
        k = length - i - 1
        for r in range(i, length - i - 1):  # offset in layer
            j = length - r - 1
            matrix[r][i], matrix[k][r] = matrix[k][r], matrix[r][i]
            matrix[k][r], matrix[j][k] = matrix[j][k], matrix[k][r]
            matrix[j][k], matrix[i][j] = matrix[i][j], matrix[j][k]
    print(matrix)


def rotate_90(matrix):
    print("rotate_90")
    print_matrix(matrix)

    # transpose
    for r in range(len(matrix)):
        for c in range(r):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    print_matrix(matrix)

    # flip it
    for row in matrix:
        row.reverse()

    print_matrix(matrix)


def rotate_270(matrix):  # -90
    print("rotate_270")
    print_matrix(matrix)

    # flip it
    for row in matrix:
        row.reverse()

    print_matrix(matrix)

    # transpose
    for r in range(len(matrix)):
        for c in range(r):
            matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

    print_matrix(matrix)


def rotate_180(matrix):
    print("rotate_180")
    top = 0
    bottom = len(matrix) - 1

    print_matrix(matrix)

    while top < bottom:
        matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
        top += 1
        bottom -= 1

    # flip it
    for row in matrix:
        row.reverse()

    print_matrix(matrix)


def print_matrix(matrix):
    for row in matrix:
        print(row)
    print("-----------")


if __name__ == "__main__":
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    rotate_90(matrix)

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    rotate_270(matrix)

    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    rotate_180(matrix)
