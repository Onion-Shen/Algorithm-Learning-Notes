from typing import List, Any, Tuple

"""
    c[i][j] means the length of x[i] and y[i].if i = 0 or j = 0, the length of seq is 0,
    then the length of LCS is 0

                0                                   if i = 0 or j = 0
    c[i][j] =   c[i - 1][j - 1] + 1                 if i,j > 0 and x[i]  = y[j]
                max(c[i][j - 1],c[i - 1][j])        if i,j > 0 and x[i] != y[j]
"""


def LCS_length(X: List[Any], Y: List[Any]) -> Tuple[List[List[Any]], List[List[Any]]]:
    m, n = len(X), len(Y)

    # b[m + 1][n + 1]
    b = [None] * (m + 1)
    for i in range(m + 1):
        b[i] = [None] * (n + 1)

    # c[m + 1][n + 1]
    c = [None] * (m + 1)
    for i in range(m + 1):
        c[i] = [None] * (n + 1)

    for i in range(m + 1):
        c[i][0] = 0

    for j in range(n + 1):
        c[0][j] = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):

            x, y = X[i - 1], Y[j - 1]

            if x == y:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = "up_left"
            else:
                c_left = c[i - 1][j]
                c_up = c[i][j - 1]

                if c_left >= c_up:
                    c[i][j] = c_left
                    b[i][j] = "up"
                else:
                    c[i][j] = c_up
                    b[i][j] = "left"

    return (c, b)


def print_LCS(b: List[List[Any]], X: List[Any], i: int, j: int):
    if i == 0 or j == 0:
        return

    b_val = b[i][j]
    if b_val == "up_left":
        print_LCS(b, X, i - 1, j - 1)
        print(X[i - 1])
    elif b_val == "up":
        print_LCS(b, X, i - 1, j)
    else:
        print_LCS(b, X, i, j - 1)
