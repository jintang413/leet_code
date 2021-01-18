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
