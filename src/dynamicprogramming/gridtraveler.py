def grid_traveler_rec(m, n):
    """ grid mxn, can only do right or down
        example 2x3
         -------------
         | S |   |   |
         |-----------|
         |   |   | E |
         |-----------|

         R->R->D
         R->D->R
         D->R->R

         grid 1x1, only 1 way
    """
    if m == n == 1:
        return 1
    ans = 0
    if m > 1:
        ans += grid_traveler_rec(m-1, n)
    if n > 1:
        ans += grid_traveler_rec(m, n-1)

    return ans

def grid_traveler_memo(m, n, memo):
    if m == n == 1:
        return 1

    if (m, n) not in memo:
        ans = 0
        if m > 1:
            ans += grid_traveler_memo(m - 1, n, memo)
        if n > 1:
            ans += grid_traveler_memo(m, n - 1, memo)
        memo[(m, n)] = ans
    return memo[(m, n)]

def grid_traveler_dp(m, n):
    """ mxn = 2x3
        dp =        [[1,1,1]
                    [1,1,1]]
        (1, 1)      [[1,1,1]  dp[1][1] = dp[0][1] + dp[1][0]
                    [1,2,1]]
        (1, 2)      [[1,1,1]
                    [1,2,3]] dp[1][2] = dp[0][2] + dp[1][1]
        ==> dp[i][j] = dp[i-1][j] + dp[i][j-1]
    """
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]
print(grid_traveler_rec(1, 1))
print(grid_traveler_rec(2, 1))
print(grid_traveler_memo(20, 20, {}))
print(grid_traveler_dp(20,20))